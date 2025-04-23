import Nav from "./components/Nav";
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
        return <></>;
    }

    const [first, second, ...rest] = data["title"].split(" ");
    const date = `${first} ${second}`;
    const title = rest.join(" ");

    return (
        <div className="p-12">
            <div className="text-center text-xl pb-4">{date}</div>
            <div className="font-bold text-4xl text-center pb-8">{title}</div>
            <div className="flex justify-center gap-10">
                <Nav />
                <div className="flex flex-col gap-4 w-150">
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
