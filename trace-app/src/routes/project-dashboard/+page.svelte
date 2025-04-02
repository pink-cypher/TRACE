<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from "svelte";
	import SettingsPopup from '$lib/settings/SettingsPopup.svelte';
	import DeleteProjectPopup from "$lib/delete/DeleteProjectPopup.svelte";
	import CreateProjectPopup from "$lib/create/CreateProjectPopup.svelte";

	type Project = {
      id: string;
      title: string;
      description: string;
      owner: string;
      status: "Active" | "Archived";
      startDate: string;
      locked: boolean;
    };

	let content = "";
	
	let showDeletePopup = false;
	let showCreatePopup = false;
	
	let projects: Project[] = [];
    let search = "";
    let loading = true;
    let error = "";

	let initials = "";
	let role = "";
	let showSettings = false;

	let projectTab = true;
	let deleteTab = false;
	let settingTab = false;
	let CreateTab = false;

	onMount(() => {
		initials = localStorage.getItem("initials");
		role = localStorage.getItem("role");

		if (!initials || !role) {
			window.location.href = "/login";
		}
	});

	onMount(async () => {
	loading = true;
    try {
      const response = await fetch('/api/projects/list', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
      });

      if (!response.ok) {
        throw new Error('Failed to fetch projects');
      }
      const data = await response.json();
  
        projects = data.projects.map((item: any) => ({
          id: item.id,
          title: item.name,
          description: item.description,
          owner: item.owner,
          status: item.status,
          startDate: item.timestamp,
          locked: item.lockStatus
        }));
      } catch (err) {
        error = "Failed to load projects.";
        console.error(err);
      } finally {
        loading = false;
      }
    });

	async function exportToFile(project_id: string, project_title: string) {
		try {
			// Fetch data from backend (adjust endpoint as needed)
			const response = await fetch("/api/projects/export", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
                // id and CSV are hardcode to test 
				body: JSON.stringify({
					id: project_id, 
					format: "CSV"
				})
			});

			if (!response.ok) {
				throw new Error("Export failed from backend");
			}

			// Get CSV content from backend response
			const data = await response.text();
			content = data;
			// Show Save Dialog
			// @ts-ignore: showSaveFilePicker is not recognized by TypeScript
			const handle = await window.showSaveFilePicker({
				suggestedName: project_title+"_project_data.csv",
				types: [
					{
						description: "CSV File",
						accept: {
							"text/csv": [".csv"]
						}
					}
				]
			});
		// Write content to chosen file
		const writable = await handle.createWritable();
			await writable.write(content);
			await writable.close();

			alert("File saved successfully!");
		} catch (err) {
			console.error("Export failed", err);
			alert("Export failed. See console for details.");
		}
	}
	async function saveProject(project_id: string) {

		console.log(project_id);
		try {
			const response = await fetch("/api/projects/save", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					projectID: project_id
				})
			});

			if (!response.ok) {
				throw new Error("Save failed from backend");
			}

			alert("Project saved successfully!");
		} catch (err) {
			console.error("Save failed", err);
			alert("Save failed. See console for details.");
		}
	}


	function logout() {
		localStorage.clear();
		window.location.href = "/login";
	}

	function activateTab(tab) {
		projectTab = tab === 'projects';
		CreateTab = tab === 'Create';
		deleteTab = tab === 'delete';
		settingTab = tab === 'settings';
	}
	function openDeletePopup() {
    	showDeletePopup = true;
 	}
  	function closeDeletePopup() {
    	showDeletePopup = false;
  	}
	function openCreatePopup() {
		showCreatePopup = true;
	}
	function closeCreatePopup() {
		showCreatePopup = false;
	}
  

	$: filteredProjects = projects.filter((p) =>
      p.title.toLowerCase().includes(search.toLowerCase())
    );
  
    // function toggleLock(project: Project) {
    //   project.locked = !project.locked;
	//   projects = [...projects];
    // }

	async function toggleLock(project: Project){
		const newState = !project.locked
		project.locked = newState;
		projects = [...projects];
		const response = await fetch("/api/projects/lock",{
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				id: project.id,
				lock: newState
			})
		})
	}

  
    function copyId(id: string) {
      navigator.clipboard.writeText(id);
      alert(`Copied project ID: ${id}`);
    }
  
    function openProject(title: string) {
      alert(`Opening project: ${title}`);
    }

</script>

<div class="layout">
	<!-- Sidebar -->
	<aside class="sidebar">
		<div class="user-info">
			<div class="initials-circle">{initials}</div>
			<div class="role">{role}</div>
		</div>

		<div class="sidebar-icons">
			<div class="sidebar-section">
				<button
					class:active-icon={projectTab}
					on:click={() => goto("/project-dashboard") }
					title="Projects"
				>
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.75V12A2.25 2.25 0 0 1 4.5 9.75h15A2.25 2.25 0 0 1 21.75 12v.75m-8.69-6.44-2.12-2.12a1.5 1.5 0 0 0-1.061-.44H4.5A2.25 2.25 0 0 0 2.25 6v12a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9a2.25 2.25 0 0 0-2.25-2.25h-5.379a1.5 1.5 0 0 1-1.06-.44Z" />
					</svg>
					<span class="icon-label">Projects</span>
				</button>
			</div>

			{#if role === "Lead"}
				<div class="sidebar-section">
					<button
						class:active-icon={deleteTab}
						on:click={() => activateTab("delete")}
						on:click={openDeletePopup}
						title="Delete Project"
					>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
						</svg>
						<span class="icon-label">Delete Project</span>
					</button>

					<button
						class:active-icon={CreateTab}
						on:click={() => activateTab("Create")}
						on:click={openCreatePopup}
						title="Create Project"
					>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
						</svg>
						<span class="icon-label">Create Project</span>
				
				</div>
			{/if}
 
			<div class="settings">
				<button 
					class:active-icon={settingTab}
					on:click={() => {
						activateTab("settings");
						showSettings = true;

					}}
					title="Settings"
				>
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" d="M11.42 15.17 17.25 21A2.652 2.652 0 0 0 21 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 1 1-3.586-3.586l6.837-5.63m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 0 0 4.486-6.336l-3.276 3.277a3.004 3.004 0 0 1-2.25-2.25l3.276-3.276a4.5 4.5 0 0 0-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085m-1.745 1.437L5.909 7.5H4.5L2.25 3.75l1.5-1.5L7.5 4.5v1.409l4.26 4.26m-1.745 1.437 1.745-1.437m6.615 8.206L15.75 15.75M4.867 19.125h.008v.008h-.008v-.008Z" />
					</svg>
					<span class="icon-label">Settings</span>
				</button>
			</div>
		</div>

		<!-- Logout Container -->
		<div class="logout-wrapper">
			<button class="logout" on:click={logout}>Log Out</button>
		</div>
	</aside>

	<!-- Main Content -->
	<main class="main">
		<header class="header">
			<h1>Projects</h1>
		</header>
		<p>This is the project dashboard where you can manage all your projects.</p>
		<div class="search-bar">
			<input
				type="text"
				placeholder="Search projects..."
				bind:value={search}
				class="input-field"
			/>
		</div>
		{#if showDeletePopup}
  			<DeleteProjectPopup on:close={closeDeletePopup} />
		{/if}
		{#if showCreatePopup}
			<CreateProjectPopup on:close={closeCreatePopup} />
		{/if}
		{#if loading}
			<p class="text-center text-gray-500">Loading projects...</p>
	  	{:else if error}
			<p class="text-center text-red-500">{error}</p>
	  	{:else if filteredProjects.length === 0}
			<p class="text-center text-gray-500">No projects found.</p>
	  	{:else}
		  <div class="project-scroll-wrapper">
			<div class="project-list">
			  {#each filteredProjects as project}
				<div class="project-card">
				  <div class="project-header">
					<h2 class="project-title">{project.title}</h2>
					<span
					  class={`status-pill ${
						project.status === "Active"
						  ? "status-active"
						  : "status-archived"
					  }`}
					>
					  {project.status}
					</span>
				  </div>
	  
				  <p class="project-description">{project.description}</p>
	  
				  <div class="project-details">
					<div><strong>Owner:</strong> {project.owner}</div>
					<div>
					  <strong>Start Date:</strong>
					  {new Date(project.startDate).toLocaleDateString()}
					</div>
					<div>
					  <strong>Lock:</strong>

					
					  <button
						class={`lock-button ${project.locked ? "locked" : "unlocked"}`}
					    on:click={() => { if (role === "Lead") toggleLock(project); }}
					  	disabled={role !== "Lead"} 
						>
						{project.locked ? "Locked" : "Unlocked"}
					  </button>


					</div>
				  </div>
	  
				  <div class="project-actions">
					<button on:click={() => copyId(project.id)}>Copy ID</button>
					<button on:click={() => openProject(project.title)}>Open</button>
					<button on:click={() => saveProject(project.id)}>Save</button>
					<button on:click={() => exportToFile(project.id,project.title)}>Export</button>
					<!-- connect export logic -->
				  </div>
				</div>
			  {/each}
			</div>
		  </div>
		{/if}
	</main>

	<SettingsPopup open={showSettings} onClose={() => showSettings = false} />
</div>

<style>
	.layout {
		display: flex;
		min-height: 100vh;
		font-family: "Raleway", sans-serif;
		background: #f9f9f9;
	}

	.sidebar {
		width: 80px;
		background: linear-gradient(to bottom, #000000, #0f172a);
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 1rem 0;
		border-top-right-radius: 10px;
		border-bottom-right-radius: 10px;
		color: #fff;
		box-shadow: 2px 0 6px rgba(0, 0, 0, 0.05);
		position: fixed;
		top: 0;
		left: 0;

		height: 100vh;
	}

	.user-info {
		text-align: center;
		font-size: 0.75rem;
		margin-bottom: 2rem;
		color: #cbd5e1;
	}

	.initials-circle {
		width: 36px;
		height: 36px;
		border-radius: 50%;
		background-color: #334155;
		color: white;
		display: flex;
		align-items: center;
		justify-content: center;
		font-weight: bold;
		margin: 0 auto 0.25rem;
	}

	.sidebar-icons {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
		align-items: center;
		flex-grow: 1;
		justify-content: center;
		width: 100%;
	}

	.sidebar-section button,
	.settings button {
		background: none;
		border: none;
		cursor: pointer;
		transition: transform 0.2s ease, background 0.2s;
		padding: 0.75rem;
		border-radius: 12px;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
		flex-direction: column;
	}

	.sidebar-section button:hover,
	.settings button:hover {
		transform: scale(1.3);
		background: rgba(255, 255, 255, 0.12);
	}

	.active-icon {
		background: rgba(255, 255, 255, 0.2);
	}

	svg {
		width: 32px;
		height: 32px;
		stroke: #cbd5e1;
	}

	.icon-label {
		font-size: 0.8rem;
		margin-top: 0.5rem;
		color: #cbd5e1;
		display: block;
	}

	.logout-wrapper {
		margin-top: auto;
		padding-bottom: 1rem;
		width: 100%;
		display: flex;
		justify-content: center;
	}

  .logout {
    padding: 0.5rem 1rem;
    background: #334155;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    font-size: 0.75rem;
    width: 90%;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  .logout:hover {
    background: #1e293b;
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  }

	.logout:hover {
		background: #1e293b;
	}

	.main {
		flex: 1;
		padding: 2rem;
		margin-left: 80px; /* same as sidebar width */
		
	}

	.header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 2rem;
	}

	.search-bar {
    margin-bottom: 1.5rem;
  	}

	.search-input {
    width: 100%;
    max-width: 400px;
    padding: 0.6rem 1rem;
    border: 1px solid #ccc;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    outline: none;
    transition: border 0.2s, box-shadow 0.2s;
    }

	.search-input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  }

  .project-scroll-wrapper {
    max-height: 80vh;
    overflow-y: auto;
    padding-right: 4px;
  }

  .project-scroll-wrapper::-webkit-scrollbar {
    width: 6px;
  }

  .project-scroll-wrapper::-webkit-scrollbar-thumb {
    background-color: rgba(100, 116, 139, 0.4);
    border-radius: 4px;
  }

  .project-scroll-wrapper::-webkit-scrollbar-thumb:hover {
    background-color: rgba(100, 116, 139, 0.6);
  }

  .project-list {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  .project-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 1rem;
    padding: 1.25rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .project-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
  }

  .project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }

  .project-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1f2937;
  }

  .status-pill {
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    border-radius: 9999px;
    font-weight: 500;
    text-transform: capitalize;
  }

  .status-active {
    background-color: #d1fae5;
    color: #065f46;
  }

  .status-archived {
    background-color: #f3f4f6;
    color: #6b7280;
  }

  .project-description {
    color: #4b5563;
    font-size: 0.875rem;
    margin-bottom: 0.75rem;
  }

  .project-details {
    font-size: 0.8125rem;
    color: #374151;
    margin-bottom: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }

  .lock-button {
    margin-left: 0.5rem;
    font-size: 0.75rem;
    padding: 0.25rem 0.75rem;
    border-radius: 0.375rem;
    font-weight: 500;
    border: none;
    cursor: pointer;
    transition: background 0.2s;
  }

  .locked {
    background-color: #fee2e2;
    color: #991b1b;
  }

  .locked:hover {
    background-color: #fecaca;
  }

  .unlocked {
    background-color: #dbeafe;
    color: #1e3a8a;
  }

  .unlocked:hover {
    background-color: #bfdbfe;
  }

  .project-actions {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    font-size: 0.8125rem;
    margin-top: 0.75rem;
  }

  .project-actions button {
    color: #2563eb;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    transition: color 0.2s;
  }

  .project-actions button:hover {
    text-decoration: underline;
    color: #1d4ed8;
  }

</style>

<!-- Check something -->