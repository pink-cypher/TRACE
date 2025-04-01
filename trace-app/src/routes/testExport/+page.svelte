<script>
	let content = "";

	async function exportToFile() {
		try {
			// Fetch data from backend (adjust endpoint as needed)
			const response = await fetch("/api/projects/export", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
                // id and CSV are hardcode to test 
				body: JSON.stringify({
					id: "4:9b85307e-5220-4f24-9712-4a463db95510:0", 
					format: "CSV"
				})
			});

			if (!response.ok) {
				throw new Error("Export failed from backend");
			}

			// Get CSV content from backend response
			const data = await response.text();
			content = data;

			// Show Save Dialog
			const handle = await window.showSaveFilePicker({
				suggestedName: "project_data.csv",
				types: [
					{
						description: "CSV File",
						accept: {
							"text/csv": [".csv"]
						}
					}
				]
			});

			// Write content to chosen file
			const writable = await handle.createWritable();
			await writable.write(content);
			await writable.close();

			alert("File saved successfully!");
		} catch (err) {
			console.error("Export failed", err);
			alert("Export failed. See console for details.");
		}
	}
</script>

<button on:click={exportToFile}>Download Exported File</button>