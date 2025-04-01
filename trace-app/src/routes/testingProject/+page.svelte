<script lang="ts">
    import { onMount } from "svelte";
  
    type Project = {
      id: string;
      title: string;
      description: string;
      owner: string;
      status: "Active" | "Archived";
      startDate: string;
      locked: boolean;
    };
  
    let projects: Project[] = [];
    let search = "";
    let loading = true;
    let error = "";
  
    onMount(async () => {
      try {
        const res = await fetch("/api/projects/list", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          }
        });
  
        const data = await res.json();
  
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
  
    $: filteredProjects = projects.filter((p) =>
      p.title.toLowerCase().includes(search.toLowerCase())
    );
  
    function toggleLock(project: Project) {
      project.locked = !project.locked;
    }
  
    function copyId(id: string) {
      navigator.clipboard.writeText(id);
      alert(`Copied project ID: ${id}`);
    }
  
    function openProject(title: string) {
      alert(`Opening project: ${title}`);
    }
  </script>
  
  <div class="page-container">
    <div class="search-bar">
      <input
        type="text"
        placeholder="Search projects..."
        bind:value={search}
        class="search-input"
      />
    </div>
  
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
                    class={`lock-button ${
                      project.locked ? "locked" : "unlocked"
                    }`}
                    on:click={() => toggleLock(project)}
                  >
                    {project.locked ? "Locked" : "Unlocked"}
                  </button>
                </div>
              </div>
  
              <div class="project-actions">
                <button on:click={() => copyId(project.id)}>Copy ID</button>
                <button on:click={() => openProject(project.title)}>Open</button>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  </div>
  
  <style>
    .page-container {
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
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