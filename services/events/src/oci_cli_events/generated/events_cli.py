# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('events.events_root_group.command_name', 'events'), cls=CommandGroupWithAlias, help=cli_util.override('events.events_root_group.help', """API for the Events Service. Use this API to manage rules and actions that create automation
in your tenancy. For more information, see [Overview of Events]."""), short_help=cli_util.override('events.events_root_group.short_help', """Events API"""))
@cli_util.help_option_group
def events_root_group():
    pass


@click.command(cli_util.override('events.rule_group.command_name', 'rule'), cls=CommandGroupWithAlias, help="""The configuration details of an Events rule. For more information, see [Managing Rules for Events]""")
@cli_util.help_option_group
def rule_group():
    pass


events_root_group.add_command(rule_group)


@rule_group.command(name=cli_util.override('events.change_rule_compartment.command_name', 'change-compartment'), help=u"""Moves a rule into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--rule-id', required=True, help=u"""The [OCID] of this rule.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_rule_compartment(ctx, from_json, rule_id, compartment_id, if_match):

    if isinstance(rule_id, six.string_types) and len(rule_id.strip()) == 0:
        raise click.UsageError('Parameter --rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('events', ctx)
    result = client.change_rule_compartment(
        rule_id=rule_id,
        change_rule_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rule_group.command(name=cli_util.override('events.create_rule.command_name', 'create'), help=u"""Creates a new rule.""")
@cli_util.option('--display-name', required=True, help=u"""A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether or not this rule is currently enabled.

Example: `true`""")
@cli_util.option('--condition', required=True, help=u"""A filter that specifies the event that will trigger actions associated with this rule. A few important things to remember about filters:

* Fields not mentioned in the condition are ignored. You can create a valid filter that matches all events with two curly brackets: `{}`

  For more examples, see [Matching Events with Filters]. * For a condition with fileds to match an event, the event must contain all the field names listed in the condition. Field names must appear in the condition with the same nesting structure used in the event.

  For a list of reference events, see [Services that Produce Events]. * Rules apply to events in the compartment in which you create them and any child compartments. This means that a condition specified by a rule only matches events emitted from resources in the compartment or any of its child compartments. * The condition is a string value in a JSON object, but numbers in conditions are converted from strings to numbers before they are evaluated for matches. This means that 100, 100.0 or 1.0e2 are all considered equal. * Boolean values are converted to numbers and then evaluated. This means true and True are considered equal, as are False and false. * Wildcard matching is supported with the asterisk (*) character.

  For examples of wildcard matching, see [Matching Events with Filters]

Example: `\\\"eventType\\\": \\\"com.oraclecloud.databaseservice.autonomous.database.backup.end\\\"`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which this rule belongs.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'events', 'class': 'ActionDetailsList'}, 'freeform-tags': {'module': 'events', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'events', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'events', 'class': 'ActionDetailsList'}, 'freeform-tags': {'module': 'events', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'events', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'events', 'class': 'Rule'})
@cli_util.wrap_exceptions
def create_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, is_enabled, condition, compartment_id, actions, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['isEnabled'] = is_enabled
    details['condition'] = condition
    details['compartmentId'] = compartment_id
    details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if description is not None:
        details['description'] = description

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('events', ctx)
    result = client.create_rule(
        create_rule_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_rule') and callable(getattr(client, 'get_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@rule_group.command(name=cli_util.override('events.delete_rule.command_name', 'delete'), help=u"""Deletes a rule.""")
@cli_util.option('--rule-id', required=True, help=u"""The [OCID] of this rule.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, rule_id, if_match):

    if isinstance(rule_id, six.string_types) and len(rule_id.strip()) == 0:
        raise click.UsageError('Parameter --rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('events', ctx)
    result = client.delete_rule(
        rule_id=rule_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_rule') and callable(getattr(client, 'get_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_rule(rule_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@rule_group.command(name=cli_util.override('events.get_rule.command_name', 'get'), help=u"""Retrieves a rule.""")
@cli_util.option('--rule-id', required=True, help=u"""The [OCID] of this rule.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'events', 'class': 'Rule'})
@cli_util.wrap_exceptions
def get_rule(ctx, from_json, rule_id):

    if isinstance(rule_id, six.string_types) and len(rule_id.strip()) == 0:
        raise click.UsageError('Parameter --rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('events', ctx)
    result = client.get_rule(
        rule_id=rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rule_group.command(name=cli_util.override('events.list_rules.command_name', 'list'), help=u"""Lists rules for this compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which this rule belongs.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only rules that match the lifecycle state in this parameter.

Example: `Creating`""")
@cli_util.option('--display-name', help=u"""A filter to return only rules with descriptions that match the displayName string in this parameter.

Example: `\"This rule sends a notification upon completion of DbaaS backup.\"`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "ID", "DISPLAY_NAME"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `timeCreated`

* **TIME_CREATED:** Sorts by timeCreated. * **DISPLAY_NAME:** Sorts by displayName. * **ID:** Sorts by id.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order.

* **ASC:** Ascending sort order. * **DESC:** Descending sort order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'events', 'class': 'list[RuleSummary]'})
@cli_util.wrap_exceptions
def list_rules(ctx, from_json, all_pages, page_size, compartment_id, limit, page, lifecycle_state, display_name, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('events', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_rules,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_rules,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_rules(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rule_group.command(name=cli_util.override('events.update_rule.command_name', 'update'), help=u"""Updates a rule.""")
@cli_util.option('--rule-id', required=True, help=u"""The [OCID] of this rule.""")
@cli_util.option('--display-name', help=u"""A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether or not this rule is currently enabled.

Example: `true`""")
@cli_util.option('--condition', help=u"""A filter that specifies the event that will trigger actions associated with this rule. A few important things to remember about filters:

* Fields not mentioned in the condition are ignored. You can create a valid filter that matches all events with two curly brackets: `{}`

  For more examples, see [Matching Events with Filters]. * For a condition with fileds to match an event, the event must contain all the field names listed in the condition. Field names must appear in the condition with the same nesting structure used in the event.

  For a list of reference events, see [Services that Produce Events]. * Rules apply to events in the compartment in which you create them and any child compartments. This means that a condition specified by a rule only matches events emitted from resources in the compartment or any of its child compartments. * The condition is a string value in a JSON object, but numbers in conditions are converted from strings to numbers before they are evaluated for matches. This means that 100, 100.0 or 1.0e2 are all considered equal. * Boolean values are converted to numbers and then evaluated. This means true and True are considered equal, as are False and false. * Wildcard matching is supported with the asterisk (*) character.

  For examples of wildcard matching, see [Matching Events with Filters]

Example: `\\\"eventType\\\": \\\"com.oraclecloud.databaseservice.autonomous.database.backup.end\\\"`""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'events', 'class': 'ActionDetailsList'}, 'freeform-tags': {'module': 'events', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'events', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'events', 'class': 'ActionDetailsList'}, 'freeform-tags': {'module': 'events', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'events', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'events', 'class': 'Rule'})
@cli_util.wrap_exceptions
def update_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, rule_id, display_name, description, is_enabled, condition, actions, freeform_tags, defined_tags, if_match):

    if isinstance(rule_id, six.string_types) and len(rule_id.strip()) == 0:
        raise click.UsageError('Parameter --rule-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if description is not None:
        details['description'] = description

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    if condition is not None:
        details['condition'] = condition

    if actions is not None:
        details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('events', ctx)
    result = client.update_rule(
        rule_id=rule_id,
        update_rule_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_rule') and callable(getattr(client, 'get_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
