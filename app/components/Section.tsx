import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion";

type SectionProps = {
    title: string;
    value: string;
};

export default function Section({ title, value }: SectionProps) {
    return (
        <Accordion type="single" collapsible>
            <AccordionItem value="item-1">
                <AccordionTrigger>{title}</AccordionTrigger>
                <AccordionContent>{value}</AccordionContent>
            </AccordionItem>
        </Accordion>
    );
}
