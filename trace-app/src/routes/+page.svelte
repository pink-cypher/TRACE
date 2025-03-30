<script lang="ts">
	import { goto } from '$app/navigation';
</script>

<!-- Landing Page Container -->
<div class="container">
	<!-- Left: TRACE name popping in from left and right -->
	<div class="left-panel">
        <!-- TRACE Container -->
		<div class="trace-inner">
			<span class="trace-left">TRA</span>
			<span class="trace-right">CE</span>
		</div>
	</div>

	<!-- Blurred Vertical Divider -->
	<div class="divider"></div>

	<!-- Right: Auth Buttons for Sigin and Signup-->
	<div class="right-panel">
        <!-- Authentication Container -->
		<div class="auth-box">
			<h2>Welcome</h2>
			<button class="auth-button" on:click={() => goto('/login')}>
				Sign In
			</button>
			<button class="auth-button secondary" on:click={() => goto('/create-account')}>
				Create Account
			</button>
		</div>
	</div>
</div>

<!-- CSS Style for TRACE and Welcome container -->
<style>
	@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@700&display=swap');
	@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

	/* Main Layout */
	.container {
		display: flex;
		height: 100vh;
		width: 100%;
		background-color: #f5f5f5;
	}

	/* Left - TRACE */
	.left-panel {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #e0e0e0;
	}

	.trace-inner {
		font-family: 'Fredoka', sans-serif;
		font-weight: 700;
		font-size: clamp(3rem, 8vw, 10rem);
		display: flex;
	}

	.trace-left,
	.trace-right {
		opacity: 0;
		animation: slideIn 1s ease-out forwards;
	}

	.trace-left {
		animation-name: slideInLeft;
	}

	.trace-right {
		animation-name: slideInRight;
		animation-delay: 0.3s;
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

	/* Divider */
	.divider {
		width: 4px;
		background: rgba(0, 0, 0, 0.1);
		backdrop-filter: blur(6px);
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
	}

	/* Right - Auth Buttons */
	.right-panel {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #f5f5f5;
	}

	.auth-box {
		background: white;
		padding: 3rem 2rem;
		border-radius: 1rem;
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
		text-align: center;
		width: 80%;
		max-width: 350px;
	}

	.auth-box h2 {
		font-family: 'Montserrat', sans-serif;
		margin-bottom: 2rem;
		font-size: 1.8rem;
	}

	.auth-button {
		display: block;
		width: 100%;
		padding: 0.75rem 0;
		font-size: 1.1rem;
		font-weight: bold;
		margin-bottom: 1rem;
		background-color: #000;
		color: #fff;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
	}

	.auth-button.secondary {
		background-color: #fff;
		color: #000;
		border: 2px solid #000;
	}

	/* Pop-out on Hover */
	.auth-button:hover,
	.auth-button.secondary:hover {
		transform: scale(1.05);
		box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
	}
</style>
