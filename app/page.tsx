import Section from "./components/Section";
import { sections } from "./utility.ts/consts";
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
            {sections.map((section) => (
                <Section key={section} title={section} value={data[section]} />
            ))}
        </div>
    );
}
