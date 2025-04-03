<script>
	import { goto } from '$app/navigation';
	import { onMount } from "svelte";
	import SettingsPopup from '$lib/settings/SettingsPopup.svelte';
	

	let initials = "";
	let role = "";
	let showSettings = false;

	let projectTab = false;
	let deleteTab = false;
	let settingTab = false;

	let tools = [
    { name: "Web Crawler", progress: 0, status: "Ready to Go!" },
    { name: "ML Generator", progress: 0, status: "Ready to Go!" },
    { name: "Parameter Fuzzing", progress: 0, status: "Ready to Go!" },
    { name: "Brute Force Tester", progress: 0, status: "Ready to Go!" },
    { name: "SQL Injection", progress: 0, status: "Ready to Go!" },
    { name: "HTTP Tester", progress: 0, status: "Ready to Go!" }
  ];

	onMount(() => {
		initials = localStorage.getItem("initials");
		role = localStorage.getItem("role");

		if (!initials || !role) {
			window.location.href = "/login";
		}
	});

	function logout() {
		localStorage.clear();
		window.location.href = "/login";
	}

	function activateTab(tab) {
		projectTab = tab === 'projects';
		deleteTab = tab === 'delete';
		settingTab = tab === 'settings';
	}
	/**
   	* @param {{ name: any; progress: any; status?: string; }} tool
	*/
	function handleAction(tool) {
		// Only act if progress is 0 ("Set Up" button)
		if (tool.progress === 0) {
		if (tool.name === "Web Crawler") {
			goto('/tools/crawler');
		} else if (tool.name === "ML Generator") {
			goto('/tools/ml');
		}else if (tool.name === "HTTP Tester") {
			goto('/tools/httpClient');
		} else {
			alert("This tool is not ready yet.");
		}
		} else {
		// If progress is non-zero, you could display the tool's dashboard or details.
		}
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
						title="Delete Project"
					>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
						</svg>
						<span class="icon-label">Delete Project</span>
					</button>
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
	<main class="main-content">
		<header class="crawler-header">
		  <h1>Tool Dashboard</h1>
		  <p class="subheader">Select a tool from the menu below.</p>
		</header>
		
		{#each tools as tool}
		  <div class="tool-item">
			<span>{tool.name}</span><br>
			<div class="progress-bar">
			  <div class="progress-fill" style="width: {tool.progress}%;"></div>
			</div>
			<span class="status">{tool.status}</span>
			<button class="info-btn">Info</button>
			<button class="action-btn" on:click={() => handleAction(tool)}>
			  {tool.progress === 0 ? 'Set Up' : 'View'}
			</button>
		  </div>
		{/each}
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

	/* .main {
		flex: 1;
		padding: 2rem;
	}

	.header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 2rem;
	} */
	/* Main content styles */
    .main-content {
      flex: 1;
      padding: 30px;
      max-width: 1200px;
      margin: 0 auto;
    }
  
    .crawler-header {
      margin-bottom: 30px;
      position: relative;
    }
  
    .crawler-header h1 {
      font-size: 24px;
      margin: 0;
      margin-bottom: 5px;
    }
  
    .subheader {
      font-size: 16px;
      color: #718096;
    }

	/* unknown stuff from team 11s stuff*/
	
    /* Progress indicator */
    .progress-indicator {
      display: flex;
      align-items: center;
      margin-top: 20px;
      max-width: 600px;
    }
  
    .progress-step {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }
  
    .step-circle {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background-color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      margin-bottom: 8px;
    }
  
    .progress-step.active .step-circle {
      background-color: #48BB78;
      color: white;
    }
  
    .progress-step.completed .step-circle {
      background-color: #38A169;
      color: white;
    }
  
    .progress-step span {
      font-size: 12px;
      color: #718096;
    }
  
    .progress-line {
      flex: 1;
      height: 2px;
      background-color: #e2e8f0;
      margin: 0 10px;
      margin-bottom: 30px;
    }
  
    .progress-line.completed {
      background-color: #38A169;
    }
  
    /* Form styles */
    .crawler-configuration {
      background-color: white;
      border-radius: 8px;
      padding: 30px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
  
    .form-group {
      margin-bottom: 20px;
    }
  
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-size: 14px;
      color: #4A5568;
    }
  
    .required {
      color: #E53E3E;
    }
  
    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      font-size: 16px;
      box-sizing: border-box;
    }
  
    .form-group input:focus {
      outline: none;
      border-color: #4299e1;
      box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.15);
    }
  
    .btn {
      padding: 10px 15px;
      border-radius: 4px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.2s;
    }
  
    .start-btn {
      background-color: #4299e1;
      color: white;
    }
  
    .start-btn:hover {
      background-color: #3182ce;
    }
  
    .secondary-btn {
      background-color: #e2e8f0;
      color: #4A5568;
    }
  
    .secondary-btn:hover {
      background-color: #cbd5e0;
    }
  
    .error-message {
      color: #E53E3E;
      margin-top: 15px;
      font-size: 14px;
    }
  
    /* Running and Results styles */
    .crawler-running, .crawler-results {
      background-color: white;
      border-radius: 8px;
      padding: 30px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
  
    .scan-progress {
      margin-bottom: 30px;
    }
  
    .scan-progress-icon {
      display: inline-block;
      margin-right: 10px;
    }
  
    .scan-circle {
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background-color: #48BB78;
      position: relative;
    }
  
    .scan-circle::after {
      content: '';
      position: absolute;
      top: -3px;
      left: -3px;
      right: -3px;
      bottom: -3px;
      border: 2px solid #48BB78;
      border-radius: 50%;
      opacity: 0.4;
    }
  
    .scan-progress-text {
      display: inline-block;
      font-weight: 600;
      margin-bottom: 10px;
    }
  
    .scanning-text {
      color: #718096;
      font-weight: normal;
    }
  
    .scan-progress-bar {
      height: 6px;
      background-color: #e2e8f0;
      border-radius: 3px;
      overflow: hidden;
    }
  
    .scan-progress-fill {
      height: 100%;
      background-color: #48BB78;
      border-radius: 3px;
      transition: width 0.3s ease;
    }
  
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }
  
    .metric-box {
      background-color: #f7fafc;
      padding: 15px;
      border-radius: 4px;
    }
  
    .metric-label {
      font-size: 14px;
      color: #718096;
      margin-bottom: 5px;
    }
  
    .metric-value {
      font-size: 18px;
      font-weight: 600;
    }
  
    .results-table {
      margin-bottom: 30px;
      overflow-x: auto;
    }
  
    table {
      width: 100%;
      border-collapse: collapse;
    }
  
    th, td {
      padding: 12px 15px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }
  
    thead tr {
      background-color: #f7fafc;
    }
  
    th {
      font-weight: 600;
      color: #4A5568;
    }
  
    tbody tr:nth-child(even) {
      background-color: #f7fafc;
    }
  
    .url-cell {
      max-width: 300px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
  
    .action-buttons {
      display: flex;
      gap: 10px;
    }
  
    .spacer {
      flex: 1;
    }
  
    .terminal-btn {
      background-color: #edf2f7;
    }
  
    .export-icon {
      margin-left: 8px;
      vertical-align: middle;
    }
    .main-content {
      flex: 1;
      padding: 30px;
    }
    .tool-item {
      display: flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 15px;
      padding: 10px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .progress-bar {
      flex: 1;
      height: 6px;
      background: #e2e8f0;
      border-radius: 3px;
    }
    .progress-fill {
      height: 100%;
      background: #48BB78;
      border-radius: 3px;
    }
    .info-btn, .action-btn {
      padding: 5px 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .info-btn {
      background: #e2e8f0;
    }
    .action-btn {
      background: #4299e1;
      color: white;
    }
</style>