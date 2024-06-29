<script>
    let data = [];

    async function fetchData() {
        const response = await fetch('http://localhost:5000/api/data');
        const result = await response.json();
        data = result;
    }

    fetchData();

	import FileUploader from './components/FileUploader.svelte';
</script>

<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>My Svelte App</title>
		<script defer src="/build/bundle.js"></script>
	</head>
	<body>
		<div>
			<h1>SQLite Database File Upload</h1>
			<FileUploader />
	  </div>
	</body>
</html>

<style>
</style>