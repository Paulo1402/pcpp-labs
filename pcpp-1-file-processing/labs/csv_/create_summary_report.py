import csv


class ExamReport:
    def __init__(self):
        self._fieldnames = [
            "Exam Name",
            "Number of Candidates",
            "Number of Passed Exams",
            "Number of Failed Exams",
            "Best Score",
            "Worst Score",
        ]

    def summarize_results_and_export(self, results_file, output_file):
        data = self._summarize_results(results_file)
        self._export(data, output_file)

    def _summarize_results(self, file):
        exams = {}

        with open(file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                exam = row["Exam Name"]
                candidate = row["Candidate ID"]
                score = row["Score"]
                grade = row["Grade"]

                if exam not in exams:
                    exams[exam] = {
                        "candidates": [],
                        "passed": 0,
                        "failed": 0,
                        "best_score": None,
                        "worst_score": None,
                    }

                exam_dict = exams[exam]

                if candidate not in exam_dict["candidates"]:
                    exam_dict["candidates"].append(candidate)

                if grade == "Pass":
                    exam_dict["passed"] += 1
                elif grade == "Fail":
                    exam_dict["failed"] += 1

                if exam_dict["worst_score"] is None or score < exam_dict["worst_score"]:
                    exam_dict["worst_score"] = score

                if exam_dict["best_score"] is None or score > exam_dict["best_score"]:
                    exam_dict["best_score"] = score

        summary = []

        for exam, data in exams.items():
            summary.append(
                (
                    exam,
                    len(data["candidates"]),
                    data["passed"],
                    data["failed"],
                    data["best_score"],
                    data["worst_score"],
                )
            )

        return summary

    def _export(self, data, output_file):
        with open(output_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self._fieldnames)
            writer.writerows(data)


exam_report = ExamReport()
exam_report.summarize_results_and_export(
    results_file="./csv_/exam_results.csv", output_file="./csv_/exam_report.csv"
)
