import prisma from "../../../lib/db";
import Link from "next/link";

export default async function GroupsPage({params}) {
    const group = await prisma.group?.findUnique({
        where: {
            id: String(params.id)
        }
    });

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">{group?.name}</h1>

            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {group?.map((group) => (
                    <li key={group.id} className="flex items-center justify-between px-5">
                        <Link href={`/group/${group.id}`}>{group.name}</Link>
                    </li>
                ))}
            </ul>
        </main>
    )
}