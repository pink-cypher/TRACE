<script>
	import './login.css';
	import { goto } from '$app/navigation';

	let initials = "";
	let role = "Analyst";
	let message = "";
	let isError = false;
	let loading = false;

	async function handleSignIn() {
		if (!initials.trim()) {
			message = "Please enter your initials.";
			isError = true;
			return;
		}

		loading = true;
		isError = false;
		message = "";

		try {
			const res = await fetch("/api/analyst/login", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ initials, role })
			});

			const data = await res.json();

			if (!res.ok) {
				message = data.detail || "Login failed.";
				isError = true;
			} else {
				message = `Signed in as ${data.initials} (${data.role})`;
				isError = false;

				localStorage.setItem("token", data.access_token);
				localStorage.setItem("initials", data.initials);
				localStorage.setItem("role", data.role);

				goto('/project-dashboard');
			}
		} catch (err) {
			console.error(err);
			message = "Unexpected error. Please try again.";
			isError = true;
		}

		loading = false;

		setTimeout(() => {
			message = "";
		}, 3000);
	}
</script>

<div class="container">
	<h1>Sign In</h1>

	{#if message}
		<div class="toast {isError ? 'error' : 'success'}">{message}</div>
	{/if}

	<input
		bind:value={initials}
		class="input"
		placeholder="Enter your initials"
		on:keydown={(e) => e.key === 'Enter' && handleSignIn()}
		required
	/>

	<select bind:value={role} class="dropdown">
		<option value="Analyst">Analyst</option>
		<option value="Lead">Lead</option>
	</select>

	{#if loading}
		<button class="create-btn" disabled>Signing In...</button>
	{:else}
		<button class="create-btn" on:click={handleSignIn}>Sign In</button>
	{/if}

	<a class="back-link" href="/">← Back to Home</a>
</div>
