import prisma from "../../lib/db";
import Link from "next/link";
import { createGroup } from "../../actions/actions"

export default async function GroupsPage() {
    const groups = await prisma.group?.findMany();
    const groupCount = await prisma.group?.count()

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">All Groups ({groupCount})</h1>

            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {groups?.map((group) => (
                    <li key={group.id} className="flex items-center justify-between px-5">
                        <Link href={`/group/${group.id}`}>{group.name}</Link>
                    </li>
                ))}
            </ul>

            <form action={createGroup} className="flex flex-col gap-y-2 w-[300px]">
                <input
                    type="text"
                    name="group_name"
                    placeholder="Group Name"
                    className="px-2 py1 rounded-sm font-black"
                    />
                <button type="submit" className="bg-blue-500 text-white rounded-sm">
                    Create User
                </button>
            </form>
        </main>
    )
}