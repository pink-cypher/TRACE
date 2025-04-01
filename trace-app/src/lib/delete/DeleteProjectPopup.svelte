<script>
    import { createEventDispatcher } from "svelte";
    let projectID = "";
    let errorMessage = "";
    const dispatch = createEventDispatcher();
  
    async function deleteProject() {
      if (!projectID.trim()) {
        errorMessage = "Project ID is required.";
        return;
      }
  
      try {
        const response = await fetch("/api/projects/delete", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ projectID }),
        });

        const result = await response.json();
  
        if (!response.ok) {
          throw new Error(result.error || "Failed to delete project.");
        }
  
        dispatch("close"); // Close modal after successful deletion
        alert("Project deleted successfully.");
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
      background: white;
      padding: 2rem;
      border-radius: 10px;
      width: 350px;
      text-align: center;
    }
  
    .input-field {
      width: 100%;
      padding: 0.75rem;
      margin: 1rem 0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  
    .button-group {
      display: flex;
      justify-content: space-between;
    }
  
    .btn {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
    }
  
    .btn-delete {
      background: red;
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
      <h2>Delete Project</h2>
      <p>Enter the Project ID to confirm deletion.</p>
  
      <input type="text" class="input-field" bind:value={projectID} placeholder="Project ID" />
  
      {#if errorMessage}
        <p class="error-message">{errorMessage}</p>
      {/if}
  
      <div class="button-group">
        <button class="btn btn-delete" on:click={deleteProject}>Delete</button>
        <button class="btn btn-cancel" on:click="{() => dispatch('close')}">Cancel</button>
      </div>
    </div>
  </div>
  