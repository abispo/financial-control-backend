import express, {Request, Response, Router} from "express";

const router: Router = express.Router();

router.post("/register", (req: Request, res: Response) => {
    res.json({message: "register route"})
});

router.post("/login", (req: Request, res: Response) => {
    res.json({message: "login route"})
});

export default router;