import express, { Express, NextFunction, Request, Response} from "express";
import dotenv from "dotenv";

import authRoutes from "./auth/routes";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use((req: Request, res: Response, next: NextFunction) => {
    res.setHeader("Content-Type", "application/json");
    next();
})

app.use("/auth", authRoutes);

app.get("/healthcheck", (req: Request, res: Response) => {
    res.send({
        uptime: process.uptime(),
        message: "OK",
        timestamp: new Date().toISOString().slice(0, -5) + 'Z'
    })
})

app.get("/", (req: Request, res: Response) => {
    res.json({message: "OK"})
});

app.listen(port, () => {
    console.log(`[server]: Server is running at http://localhost:${port}.`);
});
