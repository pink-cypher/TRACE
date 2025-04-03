<script lang="ts">
  import { goto } from '$app/navigation';
	import { onMount } from "svelte";
	import SettingsPopup from '$lib/settings/SettingsPopup.svelte';
  
  let url: string = 'https://juice-shop.herokuapp.com';
  let depth: number = 2;
  let pageLimit: number = 50;
  let urlPattern: string = 'https://juice-shop.herokuapp.com/drink/*';
  let userAgent: string = 'Mozilla/5.0';
  let requestDelay: number = 1000;
  let proxy: string = '8080';
  let crawledResults: any[] = [];
  let error: string = '';
  let isLoading = false;
  let currentStep: 'configuration' | 'running' | 'results' = 'configuration';
  let scanProgress: number = 30;

  // Metrics
  let runningTime: string = '75.036';
  let processedRequests: number = 352;
  let filteredRequests: number = 59;
  let requestsPerSec: string = '0.345';

  // side bar variables
  let initials = "";
	let role = "";
	let showSettings = false;

	let projectTab = false;
	let deleteTab = false;
	let settingTab = false;

  // Sample crawl results for demonstration
  const sampleResults = [
    { id: 45, url: 'https://juice-shop.herokuapp.com', title: 'OWASP Juice Shop', wordCount: 200, charCount: 1024, linksFound: 10, error: false },
    { id: 46, url: 'https://juice-shop.herokuapp.com/about', title: 'About Us', wordCount: 150, charCount: 850, linksFound: 5, error: false },
    { id: 47, url: 'https://juice-shop.herokuapp.com/contact', title: 'Contact Us', wordCount: 100, charCount: 500, linksFound: 4, error: false },
    { id: 48, url: 'https://juice-shop.herokuapp.com/login', title: 'Login', wordCount: 80, charCount: 450, linksFound: 3, error: false },
    { id: 49, url: 'https://juice-shop.herokuapp.com/register', title: 'Register', wordCount: 75, charCount: 420, linksFound: 3, error: false },
    { id: 50, url: 'https://juice-shop.herokuapp.com/products/1', title: 'Apple Juice', wordCount: 120, charCount: 600, linksFound: 8, error: false },
    { id: 51, url: 'https://juice-shop.herokuapp.com/products/2', title: 'Orange Juice', wordCount: 115, charCount: 580, linksFound: 8, error: false },
    { id: 52, url: 'https://juice-shop.herokuapp.com/faq', title: 'FAQ', wordCount: 200, charCount: 1024, linksFound: 6, error: false },
  ];

  // Simulating running time for completed scan
  function getCompletedRunningTime() {
    return '143.940';
  }

  // Simulating completed metrics
  function getCompletedMetrics() {
    return {
      processedRequests: 532,
      filteredRequests: 82,
      requestsPerSec: '0.532'
    };
  }

  function activateTab(tab) {
		projectTab = tab === 'projects';
		deleteTab = tab === 'delete';
		settingTab = tab === 'settings';
	}

  async function startCrawl() {
    if (!url) {
      error = 'Please enter a URL';
      return;
    }

    error = '';
    isLoading = true;
    currentStep = 'running';
    crawledResults = [];
    
    try {
      // In a real app, we'd call our API here
      // For demo, we'll simulate a crawler running for a few seconds
      const simulateCrawling = async () => {
        // Simulate progress updates
        for (let i = 0; i <= 100; i += 10) {
          scanProgress = i;
          await new Promise(resolve => setTimeout(resolve, 500));
          
          // Add sample results incrementally
          if (i > 0 && i % 20 === 0) {
            const resultsToShow = Math.floor(i / 100 * sampleResults.length);
            crawledResults = sampleResults.slice(0, resultsToShow);
          }
        }
        
        // Finished crawling
        currentStep = 'results';
        crawledResults = sampleResults;
        runningTime = getCompletedRunningTime();
        const completedMetrics = getCompletedMetrics();
        processedRequests = completedMetrics.processedRequests;
        filteredRequests = completedMetrics.filteredRequests;
        requestsPerSec = completedMetrics.requestsPerSec;
      };

      simulateCrawling();
      
      // This is the actual API call we would make in a real implementation
      /*
      const response = await fetch(`http://localhost:8000/crawl?url=${encodeURIComponent(url)}&depth=${depth}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });

      if (!response.ok) {
        throw new Error('Failed to crawl');
      }

      const data = await response.json();
      crawledResults = data.crawled_urls;
      currentStep = 'results';
      */
    } catch (err) {
      console.error(err);
      error = (err as Error).message;
      currentStep = 'configuration';
    } finally {
      isLoading = false;
    }
  }

  function pauseCrawl() {
    // Implement pause functionality
    alert('Crawl paused');
  }

  function stopCrawl() {
    // Confirm before stopping
    if (confirm('Are you sure you want to stop the crawl?')) {
      currentStep = 'results';
    }
  }

  function restartCrawl() {
    currentStep = 'configuration';
    crawledResults = [];
  }

  function showTerminal() {
    // Implement terminal view
    alert('Terminal view not implemented in this demo');
  }

  function logout() {
		localStorage.clear();
		window.location.href = "/login";
	}

  function exportResults() {
    // Create a CSV from the results
    let csvContent = "ID,URL,Title,Word Count,Character Count,Links Found,Error\n";
    
    crawledResults.forEach(result => {
      csvContent += `${result.id},${result.url},"${result.title}",${result.wordCount},${result.charCount},${result.linksFound},${result.error}\n`;
    });
    
    // Create a download link
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', 'crawler_results.csv');
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  async function processWithNLP() {
    // This would call the NLP API in a real implementation
    alert('Processing with NLP...');
  }

  async function generateCredentials() {
    // This would call the ML API in a real implementation
    alert('Generating credentials...');
  }
</script>


  <div class="container">
    <!-- Main Content -->
    <main class="main-content">
      <div class="crawler-header">
        <h1>Crawler</h1>
        {#if currentStep === 'configuration'}
          <span class="subheader">Configuration</span>
        {:else if currentStep === 'running'}
          <span class="subheader">Running</span>
        {:else}
          <span class="subheader">Results</span>
        {/if}

        <!-- Progress Indicator -->
        <div class="progress-indicator">
          <div class="progress-step {currentStep === 'configuration' ? 'active' : 'completed'}">
            <div class="step-circle">1</div>
            <span>Configuration</span>
          </div>
          <div class="progress-line {currentStep === 'running' || currentStep === 'results' ? 'completed' : ''}"></div>
          <div class="progress-step {currentStep === 'running' ? 'active' : currentStep === 'results' ? 'completed' : ''}">
            <div class="step-circle">2</div>
            <span>Running</span>
          </div>
          <div class="progress-line {currentStep === 'results' ? 'completed' : ''}"></div>
          <div class="progress-step {currentStep === 'results' ? 'active' : ''}">
            <div class="step-circle">3</div>
            <span>Results</span>
          </div>
        </div>
      </div>

      <!-- Configuration Screen -->
      {#if currentStep === 'configuration'}
        <div class="crawler-configuration">
          <div class="form-group">
            <label for="url">Target URL <span class="required">*</span></label>
            <input type="text" id="url" bind:value={url} placeholder="https://example.com" />
          </div>

          <div class="form-group">
            <label for="depth">Crawl Depth</label>
            <input type="number" id="depth" bind:value={depth} min="1" max="10" />
          </div>

          <div class="form-group">
            <label for="pageLimit">Limit on Number of Pages</label>
            <input type="number" id="pageLimit" bind:value={pageLimit} min="1" />
          </div>

          <div class="form-group">
            <label for="urlPattern">URL Patterns</label>
            <input type="text" id="urlPattern" bind:value={urlPattern} placeholder="https://example.com/path/*" />
          </div>

          <div class="form-group">
            <label for="userAgent">User Agent String</label>
            <input type="text" id="userAgent" bind:value={userAgent} />
          </div>

          <div class="form-group">
            <label for="requestDelay">Request Delay</label>
            <input type="number" id="requestDelay" bind:value={requestDelay} min="0" />
          </div>

          <div class="form-group">
            <label for="proxy">Proxy</label>
            <input type="text" id="proxy" bind:value={proxy} />
          </div>

          <button class="btn start-btn" on:click={startCrawl}>Start</button>

          {#if error}
            <div class="error-message">{error}</div>
          {/if}
        </div>
      {/if}

      <!-- Running Screen -->
      {#if currentStep === 'running'}
        <div class="crawler-running">
          <div class="scan-progress">
            <div class="scan-progress-icon">
              <div class="scan-circle"></div>
            </div>
            <div class="scan-progress-text">
              {scanProgress}% <span class="scanning-text">Scanning...</span>
            </div>
            <div class="scan-progress-bar">
              <div class="scan-progress-fill" style="width: {scanProgress}%"></div>
            </div>
          </div>

          <div class="metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Running Time</div>
              <div class="metric-value">{runningTime}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Processed Requests</div>
              <div class="metric-value">{processedRequests}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Filtered Requests</div>
              <div class="metric-value">{filteredRequests}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Requests/sec.</div>
              <div class="metric-value">{requestsPerSec}</div>
            </div>
          </div>

          <div class="results-table">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>URL</th>
                  <th>Title</th>
                  <th>Word Count</th>
                  <th>Character Count</th>
                  <th>Links Found</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {#each crawledResults as result}
                  <tr>
                    <td>{result.id}</td>
                    <td class="url-cell">{result.url}</td>
                    <td>{result.title}</td>
                    <td>{result.wordCount}</td>
                    <td>{result.charCount}</td>
                    <td>{result.linksFound}</td>
                    <td>{result.error ? 'True' : 'False'}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>

          <div class="action-buttons">
            <button class="btn secondary-btn" on:click={pauseCrawl}>Pause</button>
            <button class="btn secondary-btn" on:click={stopCrawl}>Stop</button>
            <button class="btn secondary-btn" on:click={restartCrawl}>Restart</button>
            <div class="spacer"></div>
            <button class="btn secondary-btn terminal-btn" on:click={showTerminal}>Show Terminal</button>
          </div>
        </div>
      {/if}

      <!-- Results Screen -->
      {#if currentStep === 'results'}
        <div class="crawler-results">
          <div class="metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Running Time</div>
              <div class="metric-value">{runningTime}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Processed Requests</div>
              <div class="metric-value">{processedRequests}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Filtered Requests</div>
              <div class="metric-value">{filteredRequests}</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Requests/sec.</div>
              <div class="metric-value">{requestsPerSec}</div>
            </div>
          </div>

          <div class="results-table">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>URL</th>
                  <th>Title</th>
                  <th>Word Count</th>
                  <th>Character Count</th>
                  <th>Links Found</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {#each crawledResults as result}
                  <tr>
                    <td>{result.id}</td>
                    <td class="url-cell">{result.url}</td>
                    <td>{result.title}</td>
                    <td>{result.wordCount}</td>
                    <td>{result.charCount}</td>
                    <td>{result.linksFound}</td>
                    <td>{result.error ? 'True' : 'False'}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>

          <div class="action-buttons">
            <button class="btn secondary-btn" on:click={restartCrawl}>Restart</button>
            <button class="btn secondary-btn" on:click={exportResults}>
              Export
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="export-icon">
                <path d="M3 17v3a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <polyline points="8 12 12 16 16 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="12" y1="2" x2="12" y2="16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <div class="spacer"></div>
            <button class="btn secondary-btn terminal-btn" on:click={showTerminal}>Show Terminal</button>
          </div>
        </div>
      {/if}
      </main>
  </div>


<style>

	svg {
		width: 32px;
		height: 32px;
		stroke: #cbd5e1;
	}


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
</style>