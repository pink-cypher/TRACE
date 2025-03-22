<script>
	let initials = "";
	let showRoleButtons = false;
	let errorMessage = "";

	async function handleKeyPress(event) {
		if (event.key === "Enter" && initials.trim() !== "") {
			try {
				const res = await fetch("/api/initials", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({ initials }),
				});

				const data = await res.json();

				if (data.capitalized_initials === true) {
					showRoleButtons = true;
					errorMessage = "";
				} else {
					showRoleButtons = false;
					errorMessage = "🚫 User does not exist. Please try again or create a new account.";
				}
			} catch (err) {
				console.error("Error sending initials:", err);
				errorMessage = "⚠️ Server error. Please try again.";
			}
		}
	}
</script>

<div class="greeting-container">
	<h1>Hello{initials ? `, ${initials}` : ""}</h1>

	{#if errorMessage}
		<div class="popup-message">{errorMessage}</div>
	{/if}

	<input
		bind:value={initials}
		placeholder="Enter your initials"
		class="initials-input"
		on:keydown={handleKeyPress}
		disabled={showRoleButtons}
	/>

	{#if showRoleButtons}
		<div class="login-prompt-container">
			<span class="prompt-left">Will you log</span>
			<span class="prompt-right">in as:</span>
		</div>

		<div class="role-buttons">
			<button class="role-button slide-left">Lead</button>
			<button class="role-button slide-right">Analyst</button>
		</div>
	{/if}
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@700&display=swap');

	.greeting-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		font-family: 'Raleway', sans-serif;
		overflow: hidden;
	}

	h1 {
		font-size: 3rem;
		margin-bottom: 1rem;
	}

	.popup-message {
		color: red;
		background-color: #ffecec;
		padding: 0.5rem 1rem;
		border: 1px solid red;
		border-radius: 8px;
		margin-bottom: 1rem;
		font-size: 1rem;
		animation: fadeIn 0.3s ease-in-out;
		text-align: center;
		max-width: 300px;
	}

	@keyframes fadeIn {
		from {
			opacity: 0;
			transform: translateY(-10px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.initials-input {
		padding: 0.5rem 1rem;
		font-size: 1.2rem;
		border-radius: 5px;
		border: 1px solid #ccc;
		outline: none;
		transition: background-color 0.3s ease;
	}

	.initials-input:disabled {
		background-color: #f0f0f0;
		color: #999;
		cursor: not-allowed;
	}

	.login-prompt-container {
		display: flex;
		font-size: 1.5rem;
		font-weight: bold;
		margin-top: 2rem;
		gap: 0.5rem;
	}

	.prompt-left,
	.prompt-right {
		opacity: 0;
		animation: slideIn 1s ease-out forwards;
	}

	.prompt-left {
		animation-name: slideInLeft;
	}

	.prompt-right {
		animation-name: slideInRight;
		animation-delay: 0.2s;
	}

	.role-buttons {
		margin-top: 1.5rem;
		display: flex;
		gap: 1.5rem;
	}

	.role-button {
		padding: 0.6rem 1.5rem;
		font-size: 1rem;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		background-color: #000;
		color: #fff;
		opacity: 0;
		animation-duration: 1s;
		animation-fill-mode: forwards;
		transition: background-color 0.3s ease;
	}

	.role-button:hover {
		background-color: #333;
	}

	.slide-left {
		animation-name: slideInLeft;
	}

	.slide-right {
		animation-name: slideInRight;
		animation-delay: 0.2s;
	}

	@keyframes slideInLeft {
		0% {
			transform: translateX(-100%);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}

	@keyframes slideInRight {
		0% {
			transform: translateX(100%);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
</style>
