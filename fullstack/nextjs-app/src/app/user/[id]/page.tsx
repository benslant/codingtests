import prisma from "../../../lib/db";

export default async function PostPage({params}) {
    const user = await prisma.user.findUnique({
        where: {
            id: String(params.id)
        },
        include: {
            groups: true
        }
    })

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">{user?.first_name} {user?.last_name}</h1>
            <p>{user?.email}</p>
            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {
                    user?.groups?.map((group) => 
                        (
                            <li key={group.id}>{group.name}</li>
                        )
                    )
                }
            </ul>
        </main>
    );
}