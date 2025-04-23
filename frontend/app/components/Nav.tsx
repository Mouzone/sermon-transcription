"use client";

import { useState } from "react";
import { sections, titleMappings } from "../utility.ts/consts";

export default function Nav() {
    const [selectedSection, setSelectedSection] = useState("");
    return (
        <nav className="sticky top-4 self-start flex flex-col gap-4 p-4 bg-white shadow rounded min-w-[170px]">
            {sections.map((section) => (
                <a
                    key={section}
                    href={`#${section}`}
                    className={`underline ${
                        selectedSection == section && "font-bold"
                    }`}
                    onClick={() => setSelectedSection(section)}
                >
                    {titleMappings[section]}
                </a>
            ))}
        </nav>
    );
}
