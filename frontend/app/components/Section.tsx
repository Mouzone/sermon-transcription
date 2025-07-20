import { titleMappings } from "../utility.ts/consts";
import { SectionLabel } from "../utility.ts/types";

type SectionProps = {
	title: SectionLabel;
	value: string;
};

export default function Section({ title, value }: SectionProps) {
	const paragraphs: string[] = JSON.parse(value);
	return (
		<div>
			<h4
				id={`${title}`}
				className="font-bold text-2xl pb-2"
			>
				{titleMappings[title]}
			</h4>
			{paragraphs.map((paragraph) => (
				<div className="indent-8 pb-4">{paragraph}</div>
			))}
		</div>
	);
}
