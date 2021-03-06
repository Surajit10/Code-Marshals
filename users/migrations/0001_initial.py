# Generated by Django 3.1.7 on 2021-05-30 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=34, null=True)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=14)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContestInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('passcode', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField(max_length=100)),
                ('starttime', models.TimeField(max_length=100)),
                ('endtime', models.TimeField(max_length=100)),
                ('rules', models.TextField(max_length=1000)),
                ('prizes', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContestQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.contestinformation')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('problem_name', models.CharField(blank=True, max_length=1000, unique=True)),
                ('authorname', models.CharField(blank=True, max_length=1000)),
                ('problem_statement', models.TextField(blank=True, null=True)),
                ('input_format', models.TextField(blank=True, max_length=1000)),
                ('constraints', models.TextField(blank=True, max_length=1000)),
                ('output_format', models.TextField(blank=True, max_length=1000)),
                ('tags', models.TextField(blank=True, max_length=1000)),
                ('sample_input', models.TextField(blank=True, max_length=1000)),
                ('sample_output', models.TextField(blank=True, max_length=1000)),
                ('explanation', models.TextField(blank=True, max_length=1000)),
                ('hidden_input', models.FileField(blank=True, null=True, upload_to=users.models.QuestionMake.user_directory_path)),
                ('hidden_output', models.FileField(blank=True, null=True, upload_to=users.models.QuestionMake.user_directory_path)),
                ('difficulty', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER'), ('Prefer not to say', 'PREFER NOT TO SAY')], default=None, max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_question', models.CharField(blank=True, max_length=1000)),
                ('name_of_user', models.CharField(blank=True, max_length=1000)),
                ('code', models.TextField(blank=True, max_length=100000)),
                ('language', models.CharField(blank=True, max_length=1000)),
                ('dt', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0)),
                ('remaining_time_in_sec', models.IntegerField(default=0)),
                ('name_of_contest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.contestquestions')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=70)),
                ('final_points', models.IntegerField(default=0)),
                ('cumulative_score', models.IntegerField(default=0)),
                ('number_of_submissions', models.IntegerField(default=0)),
                ('successful_submissions', models.IntegerField(default=0)),
                ('college_name', models.CharField(default='Nan', max_length=80)),
                ('con_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.contestquestions')),
            ],
        ),
        migrations.CreateModel(
            name='ContestUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_na', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.contestquestions')),
                ('username', models.ManyToManyField(related_name='username', to='users.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='contestquestions',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='question', to='users.QuestionMake'),
        ),
    ]
