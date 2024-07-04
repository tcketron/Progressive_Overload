<script>
    import WorkoutTable from '../../lib/components/WorkoutTable.svelte';
</script>

<nav>
    <ul>
        <li>
            <a href="/">Home</a>
        </li>
        <li>
            <a href="/data">Data</a>
        </li>
    </ul>
</nav>

<div class="container">
    <WorkoutTable type="legs" />
    <WorkoutTable type="push" />
    <WorkoutTable type="pull" />
</div>

<style>
    .container {
        text-align: center;
        padding: 1em;
        max-width: 1200px;
        margin: 0 auto;
    }
</style>