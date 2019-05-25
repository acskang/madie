      {% for 주제 in 게시판.글들.all %}
        <tr>
          <td><a href="{% url '글조회' 게시판.pk 주제.pk %}">{{ 주제.주제 }}</a></td>
          <td>{{ 주제.게시자.username }}</td>
          <td>0</td>
          <td>0</td>
          <td>{{ 주제.발행일 }}</td>
        </tr>
      {% endfor %}