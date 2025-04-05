<script>
	import './create-account.css';
	let initials = "";
	let role = "Analyst";
	let message = "";
	let isError = false;
	let loading = false;

	async function handleCreateAccount() {
		if (!initials.trim()) {
			message = "Please enter your initials.";
			isError = true;
			return;
		}

		loading = true;
		isError = false;
		message = "";

		try {
			// 1. Check if user already exists
			const checkRes = await fetch("/api/analyst/check", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ initials })
			});

			if (!checkRes.ok) throw new Error("Failed to check initials");

			const checkData = await checkRes.json();

			if (checkData.exists) {
				message = "User already exists.";
				isError = true;
			} else {
				// 2. Create the user if initials not taken
				const createRes = await fetch("/api/analyst/create", {
					method: "POST",
					headers: {
						"Content-Type": "application/json"
					},
					body: JSON.stringify({
						initials,
						role,
						islead: role === "Lead"
					})
				});

				if (!createRes.ok) throw new Error("Failed to create account");

				const createData = await createRes.json();

				if (createData.success) {
					message = `Account created for ${initials.toUpperCase()} as ${role}`;
					isError = false;
					initials = "";
					role = "Analyst";
				} else {
					message = "Failed to create account.";
					isError = true;
				}
			}
		} catch (err) {
			console.error(err);
			message = "⚠️ Unexpected error. Please try again.";
			isError = true;
		}

		loading = false;

		setTimeout(() => {
			message = "";
		}, 3000);
	}

</script>
<!-- Create Account container -->
<div class="container">

	<h1>Create Account</h1>
    <!-- isplay confermation if account created, account already exist or connection error-->
	{#if message}
		<div class="toast {isError ? 'error' : 'success'}">
			{message}
		</div>
	{/if}

    <!-- User enters Initials and can leave role default and hit enter to create account -->
	<input
		bind:value={initials}
		class="input"
		placeholder="Enter your initials"
		on:keydown={(e) => e.key === 'Enter' && handleCreateAccount()}
		required
	/>
    <!-- User selects role Lead or Analyst  -->
	<select bind:value={role} class="dropdown">
		<option value="Analyst">Analyst</option>
		<option value="Lead">Lead</option>
	</select>

    <!-- When hit create account button or hit enter show loading symbol else show Create Account-->
	{#if loading}
		<button class="create-btn" disabled>Creating...</button>
	{:else}
		<button class="create-btn" on:click={handleCreateAccount}>
			Create Account
		</button>
	{/if}
    <!-- Link to go back to landing page (HOME) -->
	<a class="back-link" href="/">← Back to Home</a>
</div>


