import prisma from "../../../lib/db";
import Link from "next/link";

export default async function GroupPage({params}) {
    const group = await prisma.group?.findUnique({
        where: {
            id: String(params.id)
        },
        include: {
            users: true
        }
    });

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">{group?.name}</h1>
            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {
                    group.users?.map((user) => 
                        (
                            <li key={user.id}>{user.email}</li>
                        )
                    )
                }
            </ul>
        </main>
    )
}