export default async function getHealth()
{
    let health

    try
    {
        let response = await fetch("http://localhost:3000/responses",
        {
            method: "GET"
        })

        if (!response.ok)
        {
            throw new Error(`HTTP ERROR ! Status: ${response.status}`)
        }

        health = await response.json()
    }
    catch (error)
    {
        console.error("Error fetching health status:", error)
        health = "Not Healthy"
    }

    return health
}