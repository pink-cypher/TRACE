<script>
	let initials = "";
</script>

<div class="greeting-container">
	<h1>
		Hello{initials ? `, ${initials}` : ""}
	</h1>

	<input
		bind:value={initials}
		placeholder="Enter your initials"
		class="initials-input"
	/>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@700&display=swap');

	.greeting-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		font-family:  'Raleway';
	}

	h1 {
		font-size: 3rem;
		margin-bottom: 1rem;
        
	}

	.initials-input {
		padding: 0.5rem 1rem;
		font-size: 1.2rem;
		border-radius: 5px;
		border: 1px solid #ccc;
		outline: none;
	}
</style>
