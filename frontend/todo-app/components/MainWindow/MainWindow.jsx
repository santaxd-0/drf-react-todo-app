import { CategoryContainer } from "./subcomponents/CategoryContainer/CategoryContainer";
import { TaskContainer } from "./subcomponents/TaskContainer/TaskContainer";

import "./main-window.css"

export const MainWindow = () => {
    return (
        <main className="main-window-style">
            <CategoryContainer />
            <TaskContainer />
        </main>
    );
}