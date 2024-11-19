<script lang="ts">
    import getHealth from "$lib/functions/getHealth"

    let health : String

    async function requestHealth()
    {
        health = await getHealth()
    }
</script>

<div class="button">
    <button on:click={requestHealth}>
        Check Backend Health
    </button>
</div>

<h1>{health}</h1>