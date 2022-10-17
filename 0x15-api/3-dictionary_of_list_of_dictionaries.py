#!/usr/bin/python3
"""Module fetches employe tasks and display on stdout."""


class Fetch:
    """Class provides fetch services."""

    def __init__(self, userId=None):
        """Initialize fetch instance."""

        if userId:
            payload = {"userId": userId}
            userInfo = requests.get(
                "https://jsonplaceholder.typicode.com/users/{:s}".format(
                    userId
                )
            ).json()

            self.userId = userId
            self.name = userInfo.get("name")
            self.userName = userInfo.get("username")
            self.todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos/",
                params=payload
            ).json()
        else:
            self.userInfo_list = requests.get(
                "https://jsonplaceholder.typicode.com/users/"
            ).json()
            self.todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos/"
            ).json()

        return None

    def project_task_one(self):
        """Return information about employee TODO list progress
        Args:
            self (object): <class 'main.Fetch'> type object
        Returns:
            Comperhensive string of employee TODO list progress
        """
        brief = "Employee {:s} is done with tasks ({:d}/{:d}):\n".format(
            self.userName,
            len(Fetch.__tasks(self.todos)["complete"]),
            len(self.todos)
        )
        completed = Fetch.__completed_tasks(
            Fetch.__tasks(self.todos)["complete"]
        )
        return [brief, completed]

    def project_task_two(self):
        """Export data in CSV format.
        Records all tasks that are owned by this employee
        Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        Args:
            self (object): <class 'main.Fetch'> type object
        Returns:
            None
        """
        with open("{:s}.csv".format(self.userId), 'w') as file:
            fieldnames = ["userId", "name", "completed", "title"]
            writer = csv.DictWriter(
                file,
                quoting=csv.QUOTE_ALL,
                fieldnames=fieldnames
            )
            for obj in deepcopy(self.todos):
                obj.pop("id", None)
                obj["name"] = self.userName
                writer.writerow(obj)
        return None

    def project_task_three(self):
        """Export data in JSON format.
        Records all tasks that are owned by this employee
        Format must be: {"USER_ID":[{"task":"TASK_TITLE","completed": \
        TASK_COMPLETED_STATUS,"username":"USERNAME"},{"task":"TASK_TITLE",\
        "completed":TASK_COMPLETED_STATUS,"username":"USERNAME"}, ... ]}
        Args:
            self (object): <class 'main.Fetch'> type object
        Returns:
            None
        """
        value_list = []

        for obj in self.todos:
            Fetch.__custom_obj_list(
                obj,
                self.userName,
                value_list
            )
        with open("{:s}.json".format(self.userId), 'w') as file:
            json.dump({self.userId: value_list}, file)

        return None

    def project_task_four(self):
        """Export all users' data in JSON format.
        Records all tasks from all employees
        Format must be: {"USER_ID":[{"username":"USERNAME","task":\
        "TASK_TITLE","completed":TASK_COMPLETED_STATUS},{"username":\
        "USERNAME","task":"TASK_TITLE","completed":TASK_COMPLETED_STATUS}\
        ,...],"USER_ID":[{"username":"USERNAME","task":"TASK_TITLE",\
        "completed":TASK_COMPLETED_STATUS},{"username":"USERNAME",\
        "task":"TASK_TITLE","completed":TASK_COMPLETED_STATUS},...]}
        Args:
            self (object): <class 'main.Fetch'> type object
        Returns:
            None
        """
        serialize_me = {}
        value_list = []
        username = ""

        for obj in self.todos:
            if not serialize_me.get(obj["userId"]):
                value_list = []
            for elem in self.userInfo_list:
                if elem["id"] == obj["userId"]:
                    username = elem["username"]
            Fetch.__custom_obj_list(
                obj,
                username,
                value_list
            )
            serialize_me[obj["userId"]] = value_list
        with open("todo_all_employees.json", 'w') as file:
            json.dump(serialize_me, file)

    @staticmethod
    def __tasks(tasks_list):
        """returns dictionary of task lists acording to completeness.
        Args:
            tasks_list (list): List of tasks fetched.
            status (str): `finished` or `unfinished`.
        Returns:
            dictionary of completed and uncompleted task lists.
        """
        status_dict = {
            "complete": [],
            "incomplete": []
        }

        for elem in tasks_list:
            if elem.get("completed") is True:
                status_dict["complete"].append(elem)
        for elem in tasks_list:
            if elem not in status_dict["complete"]:
                status_dict["incomplete"].append(elem)
        return status_dict

    @staticmethod
    def __completed_tasks(tasks_list):
        """Returns string representation of all tasks in provided list
        Args:
            tasks_list (list): List of tasks fetched.
        Returns:
            Tabulated list of completed tasks
        """
        brief = ""
        for elem in tasks_list:
            brief += "\t {:s}\n".format(elem.get("title"))
        return brief

    @staticmethod
    def __custom_obj_list(obj, userName, value_list):
        """append curated object to passed list
        Args:
            obj (object): object to extract content from.
            userName (string): username to add to custom object.
            value_list (list): list to append cureted object in.
        Returns:
            None
        """
        val = {}
        val["username"] = userName
        val["task"] = obj["title"]
        val["completed"] = obj["completed"]
        value_list.append(val)

        return None

    pass


if __name__ == "__main__":
    from copy import deepcopy
    import csv
    import json
    import requests

    fetch = Fetch()
    fetch.project_task_four()
