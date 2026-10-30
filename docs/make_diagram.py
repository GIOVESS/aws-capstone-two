import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG, PANEL, TEAL, AMBER, TEXT, MUTED = "#0b1f2a", "#10303f", "#2ec4b6", "#ffb703", "#e8f1f2", "#8fb3bd"

fig, ax = plt.subplots(figsize=(16, 8.5), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 160)
ax.set_ylim(0, 85)
ax.axis("off")


def box(x, y, w, h, title, sub="", edge=TEAL, fill=PANEL, tcolor=TEXT):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.2",
                                linewidth=1.8, edgecolor=edge, facecolor=fill))
    ax.text(x + w / 2, y + h * (0.62 if sub else 0.5), title, ha="center", va="center",
            color=tcolor, fontsize=11, fontweight="bold")
    if sub:
        ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center", color=MUTED, fontsize=8.5)


def arrow(p1, p2, color=TEAL, style="-|>", ls="-", rad=0.0):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle=style, color=color, lw=1.8, linestyle=ls,
                                connectionstyle=f"arc3,rad={rad}"))


ax.text(80, 81, "End-to-End CI/CD on AWS", ha="center", color=TEAL, fontsize=20, fontweight="bold")
ax.text(80, 77.2, "GitHub to CodePipeline to CodeBuild to ECR to CodeDeploy blue/green on ECS Fargate", ha="center",
        color=MUTED, fontsize=10.5)

# pipeline group
ax.add_patch(FancyBboxPatch((32, 42), 92, 28, boxstyle="round,pad=0.3,rounding_size=1.5",
                            linewidth=1.5, edgecolor=AMBER, facecolor="none", linestyle="--"))
ax.text(34, 67.2, "AWS CodePipeline: myapp-pipeline", color=AMBER, fontsize=10, fontweight="bold")

box(3, 49, 22, 14, "GitHub", "aws-capstone-two\nmain branch")
box(36, 49, 18, 14, "1. Source", "CodeStar\nconnection")
box(58, 49, 18, 14, "2. Build", "CodeBuild:\ntest, docker build")
box(80, 49, 18, 14, "3. Approval", "Manual review\nSNS email", edge=AMBER)
box(102, 49, 18, 14, "4. Deploy", "CodeDeployToECS\nblue/green")

arrow((25.5, 56), (35.5, 56))
arrow((54.5, 56), (57.5, 56))
arrow((76.5, 56), (79.5, 56))
arrow((98.5, 56), (101.5, 56))
ax.text(29.5, 58, "push", color=MUTED, fontsize=8, ha="center")

# ECR
box(58, 22, 18, 11, "Amazon ECR", "myapp-repo\n:sha-build, :latest")
arrow((67, 48.5), (67, 33.8))
ax.text(68.5, 40.5, "push image", color=MUTED, fontsize=8)

# CodeDeploy
box(102, 22, 18, 11, "CodeDeploy", "ECS blue/green\ntraffic shift")
arrow((111, 48.5), (111, 33.8))

# ALB + ECS
box(130, 52, 28, 14, "ALB", "Application Load Balancer\nprod :80  |  test :8080")
ax.add_patch(FancyBboxPatch((130, 20), 28, 26, boxstyle="round,pad=0.3,rounding_size=1.2",
                            linewidth=1.8, edgecolor=TEAL, facecolor=PANEL))
ax.text(144, 42.5, "ECS Fargate service", ha="center", color=TEXT, fontsize=11, fontweight="bold")
ax.text(144, 39.3, "myapp-service, 2 tasks", color=MUTED, fontsize=8.5, ha="center")
ax.text(144, 36.7, "CODE_DEPLOY controller", color=MUTED, fontsize=8.5, ha="center")
box(132, 22, 11.5, 11, "Blue TG", "live", edge=TEAL)
box(144.5, 22, 11.5, 11, "Green TG", "new version", edge=AMBER)
arrow((144, 51.5), (144, 46.8), style="<|-|>")
arrow((120.5, 27), (129.5, 27))
ax.text(125.5, 29, "shift", color=MUTED, fontsize=8, ha="center")
arrow((76.5, 24), (129.5, 22), color=MUTED, ls="--", rad=0.18)
ax.text(106, 17.2, "task pulls image", color=MUTED, fontsize=8, ha="center")

# users
box(130, 72, 28, 7, "Users", "", edge=MUTED)
arrow((144, 71.5), (144, 66.8))

# Monitoring
box(40, 3, 80, 10, "Monitoring and notifications",
    "CloudWatch alarms (unhealthy hosts, 5xx, CPU) + EventBridge pipeline FAILED rule  to  SNS email", edge=AMBER)
arrow((144, 19.5), (121, 8.5), color=MUTED, ls="--", rad=-0.2)
arrow((89, 48.5), (89, 13.8), color=MUTED, ls="--")

fig.savefig("pipeline-diagram.png", facecolor=BG, bbox_inches="tight")
print("saved")
