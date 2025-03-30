<script>
	import { onMount } from "svelte";
	let initials = "";
	let role = "";
	let token = "";

	onMount(() => {
		token = localStorage.getItem("token");
		initials = localStorage.getItem("initials");
		role = localStorage.getItem("role");

		if (!token || !initials || !role) {
			// Redirect to sign-in page if not logged in
			window.location.href = "/login";
		}
	});

	function handleLogout() {
		localStorage.clear();
		window.location.href = "/login";
	}
</script>

<div class="dashboard-container">
	<h1>Welcome, {initials}!</h1>
	<p>Your role: <strong>{role}</strong></p>

	<!-- Example feature restrictions -->
	{#if role === "Lead"}
		<p>You can create, lock, and delete projects.</p>
		<!-- Add more Lead-only UI here -->
	{:else}
		<p>You can access all tools except project creation, locking, and deletion.</p>
	{/if}

	<button class="logout-btn" on:click={handleLogout}>Log Out</button>
</div>

<style>
	.dashboard-container {
		padding: 2rem;
		text-align: center;
		font-family: 'Raleway', sans-serif;
	}

	h1 {
		font-size: 2.5rem;
		margin-bottom: 1rem;
	}

	p {
		font-size: 1.2rem;
		margin-bottom: 1.5rem;
	}

	.logout-btn {
		padding: 0.75rem 1.5rem;
		font-size: 1rem;
		background-color: #333;
		color: white;
		border: none;
		border-radius: 10px;
		cursor: pointer;
		transition: background-color 0.3s ease;
	}

	.logout-btn:hover {
		background-color: #111;
	}
</style>