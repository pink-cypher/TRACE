<script>
	let response = "";
	
	async function pingBackend() {
		const res = await fetch('/api/test/ping');
		const data = await res.json();
		response = JSON.stringify(data);
	}
</script>

<h1>Ping Backend</h1>
<button on:click={pingBackend}>Send Ping</button>

{#if response}
	<p>Response: {response}</p>
{/if}