import { titleMappings } from "../utility.ts/consts";
import { SectionLabel } from "../utility.ts/types";

type SectionProps = {
    title: SectionLabel;
    value: string;
};

export default function Section({ title, value }: SectionProps) {
    return (
        <div>
            <h4 id={`${title}`} className="font-bold text-2xl">
                {titleMappings[title]}
            </h4>
            <div>{value}</div>
        </div>
    );
}
