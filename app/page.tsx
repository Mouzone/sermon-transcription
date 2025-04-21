import supabase from "./utility.ts/supabase";

export default async function Page() {
    const { data, error } = await supabase
        .from("Sermon")
        .select("*")
        .order("created_at", { ascending: false })
        .limit(1)
        .single();

    if (error) {
        console.error("Error fetching recent data:", error);
        // You might want to handle the error differently
        return <></>;
    }

    return (
        <div>
            <div>{data["title"]}</div>
            <div>{data["anecdote"]}</div>
            <div>{data["opening prayer"]}</div>
            <div>{data["sermon"]}</div>
            <div>{data["closing prayer"]}</div>
            <div>{data["conclusion"]}</div>
        </div>
    );
}
