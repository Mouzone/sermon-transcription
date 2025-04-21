import { SectionLabel } from "./types";

export const sections: SectionLabel[] = [
    "anecdote",
    "opening_prayer",
    "sermon",
    "closing_prayer",
    "conclusion",
];

export const titleMappings: { [key in SectionLabel]: string } = {
    anecdote: "Anecdote",
    opening_prayer: "Opening Prayer",
    sermon: "Sermon",
    closing_prayer: "Closing Prayer",
    conclusion: "Conclusion",
};
