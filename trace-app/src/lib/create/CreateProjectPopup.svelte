<script>
    import { createEventDispatcher } from "svelte";
  
    let projectName = "";
    let description = "";
    let owner = "";
    let ips = "";
    let ports = "";
    let errorMessage = "";
    const dispatch = createEventDispatcher();
  
    async function createProject() {
      if (!projectName.trim() || !owner.trim()) {
        errorMessage = "Project Name and Owner are required.";
        return;
      }
  
      try {
        const response = await fetch("/api/projects/create", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            projectName,
            description,
            owner,
            ips: ips.split(","), // Convert comma-separated IPs into an array
            ports: ports.split(",") // Convert comma-separated ports into an array
          }),
        });
  
        const result = await response.json();
  
        if (!response.ok) {
          throw new Error(result.error || "Failed to create project.💀");
        }
  
        dispatch("close"); // Close modal after success
        alert("Project created successfully.");
      } catch (error) {
        errorMessage = error.message;
      }
    }
  </script>
  
  <style>
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
    }
  
    .modal-content {
      background: rgb(231, 230, 230);
      padding: 2rem;
      border-radius: 12px;
      width: 400px;
      text-align: center;
      justify-content: center;
    }
    
    .input-field {
      width: 85%;
      padding: 0.75rem;
      margin: 0.6rem 0;
      border: 1px solid #ccc;
      border-radius: 5px;
      
    }
  
    .button-group {
      display: flex;
      justify-content: space-between;
      margin-top: 1rem;
    }
  
    .btn {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
    }
  
    .btn-create {
      background: green;
      color: white;
    }
  
    .btn-cancel {
      background: gray;
      color: white;
    }
  
    .error-message {
      color: red;
      font-size: 0.9rem;
    }
  </style>
  
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div class="modal" on:click="{() => dispatch('close')}">
    <div class="modal-content" on:click|stopPropagation>
      <h2>Create Project</h2>
  
      <input type="text" class="input-field" bind:value={projectName} placeholder="Project Name" />
      <input type="text" class="input-field" bind:value={owner} placeholder="Owner Initials" />
      <textarea class="input-field" bind:value={description} placeholder="Project Description"></textarea>
      <input type="text" class="input-field" bind:value={ips} placeholder="IP Addresses (comma-separated)" />
      <input type="text" class="input-field" bind:value={ports} placeholder="Ports (comma-separated)" />
  
      {#if errorMessage}
        <p class="error-message">{errorMessage}</p>
      {/if}
  
      <div class="button-group">
        <button class="btn btn-create" on:click={createProject}>Create</button>
        <button class="btn btn-cancel" on:click="{() => dispatch('close')}">Cancel</button>
      </div>
    </div>
  </div>
  