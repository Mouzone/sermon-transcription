import { titleMappings } from "../utility.ts/consts";
import { SectionLabel } from "../utility.ts/types";

type SectionProps = {
    title: SectionLabel;
    value: string;
};

export default function Section({ title, value }: SectionProps) {
    return (
        <div className="pb-4">
            <h4 id={`${title}`} className="font-bold text-2xl pb-2">
                {titleMappings[title]}
            </h4>
            <div className="indent-8">{value}</div>
        </div>
    );
}
