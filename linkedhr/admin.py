from django.contrib import admin

from .models import Stage, Apply, Recruitment, Education, RecruitmentBranch, JobType, City, District, Villege, Position, UserProfile, Company, Branch, SkillList, Skill, Experience
# admin.site.site_header='Linkedhr administration'

admin.site.register(City)
admin.site.register(District)
admin.site.register(Villege)
admin.site.register(Position)
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Education)
admin.site.register(SkillList)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(JobType)
admin.site.register(RecruitmentBranch)
admin.site.register(Recruitment)
admin.site.register(Apply)
admin.site.register(Stage)

