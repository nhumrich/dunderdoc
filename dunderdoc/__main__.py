from .dunders import dunder_dict


def print_all():
    for c, v in dunder_dict.items():
        s = '''\
{method}: {reason}
    section: {section}
    Usage: {usage}

    Example implementation:
    {example}
    ''' \
            .format(
            method=v.method, reason=v.reason, section=v.section.value,
            usage=v.usage, example=v.example)
        print(s)

if __name__ == '__main__':
    print_all()