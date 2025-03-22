<script>
	import { colorBlindType } from '$lib/stores/accessibility';
  </script>
  
  <h1>Dashboard</h1>import FaEye from 'svelte-icons/fa/FaEye.svelte'
  
  <div class="success">✅ Project Created</div>
  <div class="error">❌ Failed to Save</div>
  
  <hr />
  
  <!-- Optional: Color blindness selector -->
  <label for="cb-mode">Color Blind Mode:</label>
  <select id="cb-mode" bind:value={$colorBlindType}>
	<option value="none">Default</option>
	<option value="deuteranopia">Deuteranopia</option>
	<option value="protanopia">Protanopia</option>
	<option value="tritanopia">Tritanopia</option>
	<option value="achromatopsia">Achromatopsia</option>
  </select> 