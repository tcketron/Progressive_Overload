<script>
    import { onMount } from 'svelte';
  
    let file = null;
  
    function handleFileUpload() {
      const formData = new FormData();
      formData.append('file', file);
  
      // Replace '/upload-table' with your Flask route handling file upload
      post('/upload-table', formData)
        .then(response => {
          console.log(response.data.message);  // Assuming you handle response properly
          alert('File uploaded successfully!');
        })
        .catch(error => {
          console.error('Error uploading file:', error);
          alert('Error uploading file. Please try again.');
        });
    }
  
    function handleFileChange(event) {
      file = event.target.files[0];
    }
  </script>
  
  <style>
    .upload-container {
      margin-top: 20px;
    }
  </style>
  
  <div class="upload-container">
    <input type="file" accept=".db,.sqlite,.sqlite3" on:change={handleFileChange} />
    <button on:click={handleFileUpload}>Upload File</button>
  </div>
  