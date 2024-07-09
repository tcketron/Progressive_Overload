<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    export let type;
    let data = [];
    let newEntries = [
        {
            exercise: '',
            sets: '',
            reps: '',
            weight: '',
            date: '',
            notes: ''
        }
    ];

    onMount(async () => {
        await fetchData();
    });

    async function fetchData() {
        data = await getData(type);
    }

    async function getData(table) {
        try {
            const response = await axios.get(`http://localhost:8081/api/${table}`);
            return response.data;
        } catch (error) {
            console.error(error);
            return [];
        }
    }

    function removeNewEntry(index) {
    newEntries = newEntries.filter((_, i) => i !== index);
    }


    function addNewEntry() {
        newEntries = [
            ...newEntries,
            {
                exercise: '',
                sets: '',
                reps: '',
                weight: '',
                date: '',
                notes: ''
            }
        ];
    }

    async function submitData() {
        try {
            for (let entry of newEntries) {
                await axios.post(`http://localhost:8081/api/${type}`, entry);
            }
            await fetchData();
            newEntries = [
                {
                    exercise: '',
                    sets: '',
                    reps: '',
                    weight: '',
                    date: '',
                    notes: ''
                }
            ];
        } catch (error) {
            console.error(error);
        }
    }
</script>

<div>
    <h1 style="color:rgb(220, 223, 228)">{type.charAt(0).toUpperCase() + type.slice(1)} Workouts</h1>
    <form on:submit|preventDefault={submitData}>
        <button type="button" class="button-74" on:click={() => removeNewEntry(newEntries.length - 1)}>-</button>
        <button type="button" class="button-74" on:click={addNewEntry}>+</button>
        <button type="submit" class="button-74">Submit</button>
        {#each newEntries as entry, index}
        <div>
            <input bind:value={entry.exercise} placeholder="Exercise" required />
            <input bind:value={entry.sets} type="number" placeholder="Sets" required />
            <input bind:value={entry.reps} type="number" placeholder="Reps" required />
            <input bind:value={entry.weight} type="number" placeholder="Weight" required />
            <input bind:value={entry.date} type="date" placeholder="Date" required />
            <input bind:value={entry.notes} placeholder="Notes" />
        </div>
        {/each}
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


<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
        color: rgb(220, 223, 228)
    }

    table, th, td {
        border: 2px solid rgb(220, 223, 228);
    }

    th, td {
        padding: 10px;
        text-align: left;
    }

    form {
        margin-bottom: 20px;
    }

    input {
        border: 2px solid black;
        background-color: rgb(95, 103, 120);
        border-radius: 4px;
    }
    
    button {
    background: rgb(95, 103, 120);
    border: none;
    padding: 15px 15px;
    border-radius: 10px;
    cursor: pointer;
    }

    button:hover {
    background: rgba(170, 170, 170, 0.062);
    transition: 0.5s;
    }

</style>