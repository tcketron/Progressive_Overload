<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    export let type;
    let data = [];
    let newData = {
        exercise: '',
        sets: '',
        reps: '',
        weight: '',
        date: '',
        notes: ''
    };

    onMount(async () => {
        await fetchData();
    });

    async function fetchData() {
        data = await getData(type);
    }

    async function getData(table) {
        try {
            const response = await axios.get(`http://localhost:5000/api/${table}`);
            return response.data;
        } catch (error) {
            console.error(error);
            return [];
        }
    }

    async function submitData() {
        try {
            await axios.post(`http://localhost:5000/api/${type}`, newData);
            await fetchData();
            newData = { exercise: '', sets: '', reps: '', weight: '', date: '', notes: '' };
        } catch (error) {
            console.error(error);
        }
    }
</script>

<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    table, th, td {
        border: 1px solid black;
    }

    th, td {
        padding: 10px;
        text-align: left;
    }

    form {
        margin-bottom: 20px;
    }
</style>

<div>
    <h1>{type.charAt(0).toUpperCase() + type.slice(1)} Workouts</h1>
    <form on:submit|preventDefault={submitData}>
        <input bind:value={newData.exercise} placeholder="Exercise" required />
        <input bind:value={newData.sets} type="number" placeholder="Sets" required />
        <input bind:value={newData.reps} type="number" placeholder="Reps" required />
        <input bind:value={newData.weight} type="number" placeholder="Weight" required />
        <input bind:value={newData.date} type="date" placeholder="Date" required />
        <input bind:value={newData.notes} placeholder="Notes" />
        <button type="submit">Add</button>
    </form>
    <table>
        <thead>
            <tr>
                <th>Exercise</th>
                <th>Sets</th>
                <th>Reps</th>
                <th>Weight</th>
                <th>Date</th>
                <th>Notes</th>
            </tr>
        </thead>
        <tbody>
            {#each data as row}
                <tr>
                    <td>{row.exercise}</td>
                    <td>{row.sets}</td>
                    <td>{row.reps}</td>
                    <td>{row.weight}</td>
                    <td>{row.date}</td>
                    <td>{row.notes}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>