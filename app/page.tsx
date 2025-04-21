import Section from "./components/Section";
import { sections, titleMappings } from "./utility.ts/consts";
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
        return <></>;
    }

    return (
        <div className="p-4">
            <div className="font-bold text-4xl text-center pb-8">
                {data["title"]}
            </div>
            <div className="flex gap-4">
                <nav className="flex flex-col gap-4 p-4">
                    {sections.map((section) => (
                        <a
                            key={section}
                            href={`#${section}`}
                            className="underline"
                        >
                            {titleMappings[section]}
                        </a>
                    ))}
                </nav>
                <div className="flex flex-col gap-4">
                    {sections.map((section) => (
                        <Section
                            key={section}
                            title={section}
                            value={data[section]}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
}
