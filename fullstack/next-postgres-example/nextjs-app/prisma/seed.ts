import { PrismaClient } from "@prisma/client"
const prisma = new PrismaClient();
import { v4 as uuidv4 } from "uuid"

async function main() {
    const ben_user_id = uuidv4()

    const ben = await prisma.user.upsert({
        where: {email: "benocaldwell@gmail.com"},
        update: {},
        create: {
            email: "benocaldwell@gmail.com",
            first_name: "ben",
            last_name: "caldwell",
            id: ben_user_id
        }
    })
    const safe = await prisma.group.upsert({
        where: {name: "safe group"},
        update: {},
        create: {
            name: "safe_group",
            id: uuidv4()
        }
    }
    )
    console.log({ben, safe})
}

main().then(async () => {
    await prisma.$disconnect();
})
.catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
});
