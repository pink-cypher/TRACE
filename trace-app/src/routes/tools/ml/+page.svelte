<script lang="ts">
    let generatedCredentials: string[] = [];
    let error: string = '';
    let runningTime: number = 0;
    let totalUsernames: number = 0;
    let totalPasswords: number = 0;
  
    async function generateCredentials() {
      error = '';
      try {
        const response = await fetch('http://localhost:8000/ml/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
  
        if (!response.ok) {
          throw new Error('Failed to generate credentials');
        }
  
        const data = await response.json();
        generatedCredentials = data.credentials; // format: ["username:password"]
        runningTime = data.running_time ?? 0;
        totalUsernames = data.total_usernames ?? 0;
        totalPasswords = data.total_passwords ?? 0;
      } catch (err) {
        error = (err as Error).message;
      }
    }
  </script>
  
  <div class="container">
    <!-- Main Content (ML) -->
    <div class="main-content">
      <h1>AI Generator</h1>
  
      <section class="config">
        <div class="config-group">
          <label>Word List *</label>
          <input type="text" value="/home/alex/Desktop/wordlist/web.txt" readonly />
          <button class="upload">Upload Wordlist</button>
        </div>
  
        <div class="options">
          <div class="option-block">
            <h3>Username</h3>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="u-chars" />
                <span class="slider round"></span>
              </label>
              <span>Characters</span>
            </div>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="u-numbers" checked />
                <span class="slider round"></span>
              </label>
              <span>Numbers</span>
            </div>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="u-symbols" checked />
                <span class="slider round"></span>
              </label>
              <span>Symbols</span>
            </div>
          <label>Length</label>
          <input type="number" value="12" />
        </div>
  
          <div class="option-block">
            <h3>Password</h3>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="p-chars" checked />
                <span class="slider round"></span>
              </label>
              <span>Characters</span>
            </div>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="p-numbers" />
                <span class="slider round"></span>
              </label>
              <span>Numbers</span>
            </div>
            <div class="toggle-group">
              <label class="switch">
                <input type="checkbox" id="p-symbols" />
                <span class="slider round"></span>
              </label>
              <span>Symbols</span>
            </div>
            <label>Length</label>
            <input type="number" value="12" />
          </div>
        </div>
      </section>
  
      <button class="generate" on:click={generateCredentials}>Generate</button>
  
      {#if error}
        <p class="error">{error}</p>
      {/if}
  
      {#if generatedCredentials.length > 0}
        <section class="stats">
          <div>
            <strong>Running Time</strong>
            <br />{runningTime.toFixed(3)}
          </div>
          <div>
            <strong>Generated Usernames</strong>
            <br />{totalUsernames}
          </div>
          <div>
            <strong>Generated Passwords</strong>
            <br />{totalPasswords}
          </div>
        </section>
  
        <section class="credentials">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Usernames</th>
                <th>Passwords</th>
              </tr>
            </thead>
            <tbody>
              {#each generatedCredentials as cred, i}
                <tr>
                  <td>{i + 1}</td>
                  <td>{cred.split(':')[0]}</td>
                  <td>{cred.split(':')[1]}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        </section>
  
        <div class="actions">
          <button class="re-generate" on:click={generateCredentials}>Re-Generate</button>
          <button class="save">Save Word List</button>
        </div>
      {/if}
    </div>
  </div>
  
  <style>
    :global(body) {
      margin: 0;
      font-family: 'Arial', sans-serif;
    }
  
    :global(.toggle-group label.switch) {
      margin-right: 8px;
    }
    /* Main Content */
    .main-content {
      flex: 1;
      padding: 2rem;
      text-align: center; /* centers titles, buttons, etc. */
    }
  
    /* White Box (Config Section) */
    .config {
      display: flex;
      flex-direction: column;
      background-color: #fff;
      padding: 1rem 2rem;
      border-radius: 10px;
      border: 1px solid #e2e8f0;
      max-width: 900px;
      margin: 0 auto 1rem auto; /* centers the box horizontally with a bottom margin */
      text-align: left; /* ensures inner elements remain left-aligned */
    }
  
    /* Container & Base */
    .container {
      display: flex;
      min-height: 100vh;
      background-color: #f5f7fa;
    }
  
   
    /* Main Content */
    .main-content {
      flex: 1;
      padding: 2rem;
    }
  
    h1 {
      font-size: 1.5rem;
      margin-bottom: 2rem;
      color: #2d3748;
    }
  
    /* ML Configuration & Options */
    .config {
      display: flex;
      flex-direction: column;
      background-color: #fff;
      padding: 1rem 2rem;
      border-radius: 10px;
      border: 1px solid #e2e8f0;
      max-width: 900px;
      margin-bottom: 1rem;
    }
  
    .config-group {
      margin-bottom: 1.5rem;
    }
  
    .config-group input[type="text"] {
      width: 100%;
      padding: 0.6rem;
      border-radius: 6px;
      border: 1px solid #cbd5e0;
      margin-top: 0.5rem;
      font-size: 0.95rem;
    }
  
    .upload {
      margin-top: 0.75rem;
      background-color: #4fd1c5;
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      font-weight: 500;
      cursor: pointer;
    }
  
    .options {
      display: flex;
      gap: 2rem;
    }
  
    .option-block {
      flex: 1;
    }
  
    .option-block h3 {
      margin-bottom: 0.5rem;
      color: #4a5568;
    }
  
    .option-block label {
      margin-left: 0.5rem;
    }
  
    .option-block input[type="number"] {
      width: 100%;
      margin-top: 0.5rem;
      padding: 0.4rem;
      border-radius: 6px;
      border: 1px solid #cbd5e0;
    }
  
    .generate {
      margin-top: 1.5rem;
      background-color: #4299e1;
      padding: 0.6rem 1.4rem;
      border-radius: 6px;
      color: white;
      font-weight: 500;
      border: none;
      cursor: pointer;
    }
  
    .generate:hover {
      background-color: #2b6cb0;
    }
  
    /* Stats, Credentials & Actions */
    .stats {
      display: flex;
      gap: 3rem;
      margin-top: 2rem;
      font-size: 1.1rem;
      color: #2d3748;
    }
  
    .credentials {
      background-color: white;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 1rem;
      margin-top: 1rem;
      max-width: 100%;
      overflow-x: auto;
    }
  
    table {
      width: 100%;
      border-collapse: collapse;
    }
  
    th, td {
      text-align: left;
      padding: 12px 16px;
      border-bottom: 1px solid #e2e8f0;
      color: #2d3748;
    }
  
    th {
      background-color: #edf2f7;
      font-weight: 600;
    }
  
    tr:nth-child(even) {
      background-color: #f7fafc;
    }
  
    .actions {
      display: flex;
      justify-content: space-between;
      max-width: 400px;
      margin-top: 1rem;
    }
  
    .re-generate, .save {
      background-color: #4a5568;
      color: white;
      border: none;
      padding: 0.6rem 1.2rem;
      border-radius: 6px;
      font-size: 1rem;
      cursor: pointer;
    }
  
    .save {
      background-color: #4299e1;
    }
  
    .error {
      color: #c62828;
      background-color: #ffebee;
      padding: 0.75rem;
      margin-top: 1rem;
      border-radius: 4px;
      max-width: 600px;
    }
  
    /* Toggle Switch Styles */
    .switch {
      position: relative;
      display: inline-block;
      width: 40px;
      height: 20px;
      margin-left: 10px;
    }
  
    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
  
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      transition: 0.4s;
    }
  
    .slider:before {
      position: absolute;
      content: "";
      height: 16px;
      width: 16px;
      left: 2px;
      bottom: 2px;
      background-color: white;
      transition: 0.4s;
    }
  
    input:checked + .slider {
      background-color: #4fd1c5;
    }
  
    input:checked + .slider:before {
      transform: translateX(20px);
    }
  
    .slider.round {
      border-radius: 20px;
    }
  
    .slider.round:before {
      border-radius: 50%;
    }
  
    .toggle-group {
      display: flex;
      align-items: center;
      margin-bottom: 0.5rem;
    }
  
    .toggle-group span {
      font-size: 0.95rem;
    }
  
  </style>