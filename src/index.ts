import express, { Express, Request, Response} from "express";
import dotenv from "dotenv";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;

app.get("/healthcheck", (req: Request, res: Response) => {
    res.send({
        uptime: process.uptime(),
        message: "OK",
        timestamp: new Date().toISOString().slice(0, -5) + 'Z'
    })
})

app.get("/", (req: Request, res: Response) => {
    res.send("OK")
});

app.listen(port, () => {
    console.log(`[server]: Server is running at http://localhost:${port}.`);
});
