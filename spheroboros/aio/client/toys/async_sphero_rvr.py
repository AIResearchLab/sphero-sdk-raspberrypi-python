#!/usr/bin/env python3
# This file is automatically generated!
# Toy Name:           Sphero RVR
# Prefix:             RV
# Command Count:      87
# Timestamp:          01/23/2019 @ 18:37:41.344164 (UTC)

import asyncio
from spheroboros.aio.common.commands import api_and_shell
from spheroboros.aio.common.commands import system_info
from spheroboros.aio.common.commands import system_mode
from spheroboros.aio.common.commands import power
from spheroboros.aio.common.commands import drive
from spheroboros.aio.common.commands import sensor
from spheroboros.aio.common.commands import connection
from spheroboros.aio.common.commands import io
from spheroboros.aio.common.commands import firmware
from spheroboros.aio.common.commands import factory_test
from spheroboros.aio.common.toys.async_sphero_toy import AsyncSpheroToy
from spheroboros.aio.client.dal.restful_async_dal import RestfulAsyncDal


class AsyncSpheroRvr(AsyncSpheroToy):
    def __init__(self, dal=RestfulAsyncDal(prefix='rv')):
        AsyncSpheroToy.__init__(self)
        self._dal = dal

    async def echo(self, data, target, timeout=None):
        '''echo

        :param data: 
        :type data: array of uint8_ts (up to 16)
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: data(uint8_t array)
        '''
        return await api_and_shell.echo(self, data, target, timeout=timeout)

    async def get_api_protocol_version(self, target, timeout=None):
        '''get_api_protocol_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major_version(uint8_t array), minor_version(uint8_t array)
        '''
        return await api_and_shell.get_api_protocol_version(self, target, timeout=timeout)

    async def send_command_to_shell(self, shell_command_string, target, timeout=None):
        '''send_command_to_shell

        :param str shell_command_string:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await api_and_shell.send_command_to_shell(self, shell_command_string, target, timeout=timeout)

    async def on_send_string_to_console(self, target, handler=None, timeout=None):
        '''send_string_to_console

        :param coroutine handler: called asynchronously, takes form handler(console_string)
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            api_and_shell.on_send_string_to_console(self, target, handler=handler, timeout=timeout)
        )

    async def get_supported_dids(self, target, timeout=None):
        '''get_supported_dids

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: dids(uint8_t array)
        '''
        return await api_and_shell.get_supported_dids(self, target, timeout=timeout)

    async def get_supported_cids(self, did, target, timeout=None):
        '''get_supported_cids

        :param uint8_t did:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: cids(uint8_t array)
        '''
        return await api_and_shell.get_supported_cids(self, did, target, timeout=timeout)

    async def get_main_application_version(self, target, timeout=None):
        '''get_main_application_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major(uint16_t array), minor(uint16_t array), revision(uint16_t array)
        '''
        return await system_info.get_main_application_version(self, target, timeout=timeout)

    async def get_bootloader_version(self, target, timeout=None):
        '''get_bootloader_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major(uint16_t array), minor(uint16_t array), revision(uint16_t array)
        '''
        return await system_info.get_bootloader_version(self, target, timeout=timeout)

    async def get_board_revision(self, target, timeout=None):
        '''get_board_revision

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: revision(uint8_t array)
        '''
        return await system_info.get_board_revision(self, target, timeout=timeout)

    async def get_mac_address(self, timeout=None):
        '''get_mac_address

        :param float timeout: maximum time to await a response

        :returns: mac_address(std::string array)
        '''
        return await system_info.get_mac_address(self, target=1, timeout=timeout)

    async def get_nordic_temperature(self, timeout=None):
        '''get_nordic_temperature

        :param float timeout: maximum time to await a response

        :returns: temperature(int32_t array)
        '''
        return await system_info.get_nordic_temperature(self, target=1, timeout=timeout)

    async def on_application_ready_notify(self, handler=None, timeout=None):
        '''application_ready_notify

        :param coroutine handler: called asynchronously, takes form handler(application_index)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            system_info.on_application_ready_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def get_stats_id(self, target, timeout=None):
        '''get_stats_id

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: stats_id(uint16_t array)
        '''
        return await system_info.get_stats_id(self, target, timeout=timeout)

    async def on_application_alive_notify(self, handler=None, timeout=None):
        '''application_alive_notify

        :param coroutine handler: called asynchronously, takes form handler(application_index)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            system_info.on_application_alive_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def get_processor_name(self, target, timeout=None):
        '''get_processor_name

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: name(std::string array)
        '''
        return await system_info.get_processor_name(self, target, timeout=timeout)

    async def get_boot_reason(self, timeout=None):
        '''get_boot_reason

        :param float timeout: maximum time to await a response

        :returns: reason(uint8_t array)
        '''
        return await system_info.get_boot_reason(self, target=1, timeout=timeout)

    async def get_last_error_info(self, timeout=None):
        '''get_last_error_info

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: file_name(uint8_t array), line_number(uint16_t array), data(uint8_t array)
        '''
        return await system_info.get_last_error_info(self, target=1, timeout=timeout)

    async def request_l1_diagnostics(self, target, timeout=None):
        '''request_l1_diagnostics

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.request_l1_diagnostics(self, target, timeout=timeout)

    async def write_config_block(self, target, timeout=None):
        '''write_config_block

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: is_success(bool array)
        '''
        return await system_info.write_config_block(self, target, timeout=timeout)

    async def get_config_block(self, target, timeout=None):
        '''get_config_block

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: meta_data_version(uint32_t array), config_block_version(uint32_t array), application_data(uint8_t array)
        '''
        return await system_info.get_config_block(self, target, timeout=timeout)

    async def set_config_block(self, meta_data_version, config_block_version, application_data, target, timeout=None):
        '''set_config_block

        :param uint32_t meta_data_version:  
        :param uint32_t config_block_version:  
        :param application_data: 
        :type application_data: array of uint8_ts (up to 255)
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.set_config_block(self, meta_data_version, config_block_version, application_data, target, timeout=timeout)

    async def erase_config_block(self, magic_safety_number, target, timeout=None):
        '''erase_config_block

        :param uint32_t magic_safety_number:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.erase_config_block(self, magic_safety_number, target, timeout=timeout)

    async def get_swd_locking_status(self, target, timeout=None):
        '''get_swd_locking_status

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: is_locked(bool array)
        '''
        return await system_info.get_swd_locking_status(self, target, timeout=timeout)

    async def set_swd_locking(self, is_locked, unlocking_key, target, timeout=None):
        '''set_swd_locking

        :param bool is_locked:  
        :param uint32_t unlocking_key:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.set_swd_locking(self, is_locked, unlocking_key, target, timeout=timeout)

    async def get_manufacturing_date(self, target, timeout=None):
        '''get_manufacturing_date

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: year(uint16_t array), month(uint8_t array), day(uint8_t array)
        '''
        return await system_info.get_manufacturing_date(self, target, timeout=timeout)

    async def set_manufacturing_date(self, year, month, day, target, timeout=None):
        '''set_manufacturing_date

        :param uint16_t year:  
        :param uint8_t month:  
        :param uint8_t day:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.set_manufacturing_date(self, year, month, day, target, timeout=timeout)

    async def set_sku(self, sku, target, timeout=None):
        '''set_sku

        :param str sku:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_info.set_sku(self, sku, target, timeout=timeout)

    async def get_sku(self, target, timeout=None):
        '''get_sku

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: sku(std::string array)
        '''
        return await system_info.get_sku(self, target, timeout=timeout)

    async def enable_play_mode_change_notify(self, timeout=None):
        '''enable_play_mode_change_notify

        :param float timeout: maximum time to await a response

        :returns: identifier(uint8_t array)
        '''
        return await system_mode.enable_play_mode_change_notify(self, target=1, timeout=timeout)

    async def set_play_mode(self, identifier, timeout=None):
        '''set_play_mode

        :param uint16_t identifier:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await system_mode.set_play_mode(self, identifier, target=1, timeout=timeout)

    async def get_play_mode(self, timeout=None):
        '''get_play_mode

        :param float timeout: maximum time to await a response

        :returns: identifier(uint16_t array)
        '''
        return await system_mode.get_play_mode(self, target=1, timeout=timeout)

    async def enter_deep_sleep(self, seconds_until_deep_sleep, timeout=None):
        '''enter_deep_sleep

        :param uint8_t seconds_until_deep_sleep:  seconds
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enter_deep_sleep(self, seconds_until_deep_sleep, target=1, timeout=timeout)

    async def enter_soft_sleep(self, timeout=None):
        '''enter_soft_sleep

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enter_soft_sleep(self, target=1, timeout=timeout)

    async def prepare_for_shutdown(self, timeout=None):
        '''prepare_for_shutdown

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.prepare_for_shutdown(self, target=2, timeout=timeout)

    async def on_ready_for_shutdown_notify(self, handler=None, timeout=None):
        '''ready_for_shutdown_notify

        :param coroutine handler: called asynchronously, takes form handler()
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_ready_for_shutdown_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def force_battery_refresh(self, timeout=None):
        '''force_battery_refresh

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.force_battery_refresh(self, target=1, timeout=timeout)

    async def wake(self, timeout=None):
        '''wake

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.wake(self, target=1, timeout=timeout)

    async def get_battery_percentage(self, timeout=None):
        '''get_battery_percentage

        :param float timeout: maximum time to await a response

        :returns: percentage(uint8_t array)
        '''
        return await power.get_battery_percentage(self, target=1, timeout=timeout)

    async def get_battery_voltage_state(self, timeout=None):
        '''get_battery_voltage_state

        :param float timeout: maximum time to await a response

        :returns: state(uint8_t array)
        '''
        return await power.get_battery_voltage_state(self, target=1, timeout=timeout)

    async def on_will_sleep_notify(self, handler=None, timeout=None):
        '''will_sleep_notify

        :param coroutine handler: called asynchronously, takes form handler()
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_will_sleep_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def on_did_sleep_notify(self, handler=None, timeout=None):
        '''did_sleep_notify

        :param coroutine handler: called asynchronously, takes form handler()
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_did_sleep_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def enable_battery_voltage_state_change_notify(self, is_enabled, timeout=None):
        '''enable_battery_voltage_state_change_notify

        :param bool is_enabled:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enable_battery_voltage_state_change_notify(self, is_enabled, target=1, timeout=timeout)

    async def on_battery_voltage_state_change_notify(self, handler=None, timeout=None):
        '''battery_voltage_state_change_notify

        :param coroutine handler: called asynchronously, takes form handler(state)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_battery_voltage_state_change_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def raw_motors(self, left_mode, left_speed, right_mode, right_speed, timeout=None):
        '''raw_motors

        :param uint8_t left_mode:  
        :param uint8_t left_speed:  
        :param uint8_t right_mode:  
        :param uint8_t right_speed:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.raw_motors(self, left_mode, left_speed, right_mode, right_speed, target=2, timeout=timeout)

    async def reset_yaw(self, timeout=None):
        '''reset_yaw

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.reset_yaw(self, target=2, timeout=timeout)

    async def drive_with_heading(self, speed, heading, flags, timeout=None):
        '''drive_with_heading

        :param uint8_t speed:  
        :param int16_t heading:  
        :param uint8_t flags: drive_flags 
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.drive_with_heading(self, speed, heading, flags, target=2, timeout=timeout)

    async def tank_drive(self, left_speed, right_speed, flags, timeout=None):
        '''tank_drive

        :param uint8_t left_speed:  
        :param uint8_t right_speed:  
        :param uint8_t flags: drive_flags 
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.tank_drive(self, left_speed, right_speed, flags, target=2, timeout=timeout)

    async def rc_drive(self, speed, turn_rate, flags, timeout=None):
        '''rc_drive

        :param uint8_t speed:  
        :param uint8_t turn_rate:  
        :param uint8_t flags: drive_flags 
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.rc_drive(self, speed, turn_rate, flags, target=2, timeout=timeout)

    async def set_stabilization(self, index, timeout=None):
        '''set_stabilization

        :param uint8_t index:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.set_stabilization(self, index, target=2, timeout=timeout)

    async def set_sensor_streaming_mask(self, interval, packet_count, data_mask, timeout=None):
        '''set_sensor_streaming_mask

        :param uint16_t interval:  
        :param uint8_t packet_count:  
        :param uint32_t data_mask:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.set_sensor_streaming_mask(self, interval, packet_count, data_mask, target=2, timeout=timeout)

    async def get_sensor_streaming_mask(self, timeout=None):
        '''get_sensor_streaming_mask

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: interval(uint16_t array), packet_count(uint8_t array), data_mask(uint32_t array)
        '''
        return await sensor.get_sensor_streaming_mask(self, target=2, timeout=timeout)

    async def on_sensor_streaming_data_notify(self, handler=None, timeout=None):
        '''sensor_streaming_data_notify

        :param coroutine handler: called asynchronously, takes form handler(sensor_data)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_sensor_streaming_data_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def get_encoder_counts(self, timeout=None):
        '''get_encoder_counts

        :param float timeout: maximum time to await a response

        :returns: encoder_counts(int16_t array)
        '''
        return await sensor.get_encoder_counts(self, target=2, timeout=timeout)

    async def get_euler_angles(self, timeout=None):
        '''get_euler_angles

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: pitch(float array), roll(float array), extended_roll(float array), yaw(float array)
        '''
        return await sensor.get_euler_angles(self, target=2, timeout=timeout)

    async def get_gyro_degrees_per_second(self, timeout=None):
        '''get_gyro_degrees_per_second

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: pitch(float array), roll(float array), yaw(float array)
        '''
        return await sensor.get_gyro_degrees_per_second(self, target=2, timeout=timeout)

    async def set_extended_sensor_streaming_mask(self, data_mask, timeout=None):
        '''set_extended_sensor_streaming_mask

        :param uint32_t data_mask:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.set_extended_sensor_streaming_mask(self, data_mask, target=2, timeout=timeout)

    async def get_extended_sensor_streaming_mask(self, timeout=None):
        '''get_extended_sensor_streaming_mask

        :param float timeout: maximum time to await a response

        :returns: data_mask(uint32_t array)
        '''
        return await sensor.get_extended_sensor_streaming_mask(self, target=2, timeout=timeout)

    async def get_rightsideupness(self, timeout=None):
        '''get_rightsideupness

        :param float timeout: maximum time to await a response

        :returns: rightsideupness(int8_t array)
        '''
        return await sensor.get_rightsideupness(self, target=2, timeout=timeout)

    async def enable_gyro_max_notify(self, is_enabled, timeout=None):
        '''enable_gyro_max_notify

        :param bool is_enabled:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.enable_gyro_max_notify(self, is_enabled, target=2, timeout=timeout)

    async def on_gyro_max_notify(self, handler=None, timeout=None):
        '''gyro_max_notify

        :param coroutine handler: called asynchronously, takes form handler(flags)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_gyro_max_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def get_bot_to_bot_infrared_readings(self, timeout=None):
        '''get_bot_to_bot_infrared_readings

        :param float timeout: maximum time to await a response

        :returns: sensor_data(uint32_t array)
        '''
        return await sensor.get_bot_to_bot_infrared_readings(self, target=2, timeout=timeout)

    async def magnetometer_calibrate_to_north(self, timeout=None):
        '''magnetometer_calibrate_to_north

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.magnetometer_calibrate_to_north(self, target=2, timeout=timeout)

    async def on_magnetometer_north_yaw_notify(self, handler=None, timeout=None):
        '''magnetometer_north_yaw_notify

        :param coroutine handler: called asynchronously, takes form handler(yaw_direction)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_magnetometer_north_yaw_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def start_robot_to_robot_infrared_broadcasting(self, far_code, near_code, timeout=None):
        '''start_robot_to_robot_infrared_broadcasting

        :param uint8_t far_code:  
        :param uint8_t near_code:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.start_robot_to_robot_infrared_broadcasting(self, far_code, near_code, target=2, timeout=timeout)

    async def start_robot_to_robot_infrared_following(self, far_code, near_code, timeout=None):
        '''start_robot_to_robot_infrared_following

        :param uint8_t far_code:  
        :param uint8_t near_code:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.start_robot_to_robot_infrared_following(self, far_code, near_code, target=2, timeout=timeout)

    async def stop_robot_to_robot_infrared_broadcasting(self, timeout=None):
        '''stop_robot_to_robot_infrared_broadcasting

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.stop_robot_to_robot_infrared_broadcasting(self, target=2, timeout=timeout)

    async def send_robot_to_robot_infrared_message(self, infrared_code, front_left_strength, front_right_strength, back_right_strength, back_left_strength, timeout=None):
        '''send_robot_to_robot_infrared_message

        :param uint8_t infrared_code:  
        :param uint8_t front_left_strength:  
        :param uint8_t front_right_strength:  
        :param uint8_t back_right_strength:  
        :param uint8_t back_left_strength:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.send_robot_to_robot_infrared_message(self, infrared_code, front_left_strength, front_right_strength, back_right_strength, back_left_strength, target=2, timeout=timeout)

    async def listen_for_robot_to_robot_infrared_message(self, infrared_code, listen_duration, timeout=None):
        '''listen_for_robot_to_robot_infrared_message

        :param uint8_t infrared_code:  
        :param uint32_t listen_duration:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.listen_for_robot_to_robot_infrared_message(self, infrared_code, listen_duration, target=2, timeout=timeout)

    async def on_robot_to_robot_infrared_message_received_notify(self, handler=None, timeout=None):
        '''robot_to_robot_infrared_message_received_notify

        :param coroutine handler: called asynchronously, takes form handler(infrared_code)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_robot_to_robot_infrared_message_received_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def get_magnetometer_chip_id(self, timeout=None):
        '''get_magnetometer_chip_id

        :param float timeout: maximum time to await a response

        :returns: chip_id(uint8_t array)
        '''
        return await sensor.get_magnetometer_chip_id(self, target=2, timeout=timeout)

    async def run_infrared_self_test(self, timeout=None):
        '''run_infrared_self_test

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.run_infrared_self_test(self, target=2, timeout=timeout)

    async def on_infrared_self_test_results_notify(self, handler=None, timeout=None):
        '''infrared_self_test_results_notify

        :param coroutine handler: called asynchronously, takes form handler(is_successfulinfrared_sensor_test_details_mask)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_infrared_self_test_results_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def set_bluetooth_device_name(self, name, target, timeout=None):
        '''set_bluetooth_device_name

        :param str name:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await connection.set_bluetooth_device_name(self, name, target, timeout=timeout)

    async def get_bluetooth_device_name(self, target, timeout=None):
        '''get_bluetooth_device_name

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: name(std::string array)
        '''
        return await connection.get_bluetooth_device_name(self, target, timeout=timeout)

    async def set_all_leds(self, led_group, led_brightness_values, timeout=None):
        '''set_all_leds

        :param uint16_t led_group: led_groups 
        :param led_brightness_values: 
        :type led_brightness_values: array of uint8_ts (up to 16)
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.set_all_leds(self, led_group, led_brightness_values, target=1, timeout=timeout)

    async def set_all_leds_with_32_bit_mask(self, led_group, led_brightness_values, timeout=None):
        '''set_all_leds_with_32_bit_mask

        :param uint32_t led_group: led_groups 
        :param led_brightness_values: 
        :type led_brightness_values: array of uint8_ts (up to 32)
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.set_all_leds_with_32_bit_mask(self, led_group, led_brightness_values, target=1, timeout=timeout)

    async def set_all_leds_with_64_bit_mask(self, led_group, led_brightness_values, timeout=None):
        '''set_all_leds_with_64_bit_mask

        :param uint64_t led_group: led_groups 
        :param led_brightness_values: 
        :type led_brightness_values: array of uint8_ts (up to 64)
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.set_all_leds_with_64_bit_mask(self, led_group, led_brightness_values, target=1, timeout=timeout)

    async def set_all_leds_with_8_bit_mask(self, led_group, led_brightness_values, timeout=None):
        '''set_all_leds_with_8_bit_mask

        :param uint8_t led_group: led_groups 
        :param led_brightness_values: 
        :type led_brightness_values: array of uint8_ts (up to 8)
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.set_all_leds_with_8_bit_mask(self, led_group, led_brightness_values, target=1, timeout=timeout)

    async def jump_to_bootloader(self, timeout=None):
        '''jump_to_bootloader

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await firmware.jump_to_bootloader(self, target=2, timeout=timeout)

    async def set_test_fixture_result(self, test_id, fixture_id, results, timeout=None):
        '''set_test_fixture_result

        :param uint16_t test_id:  
        :param uint16_t fixture_id:  
        :param uint32_t results:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await factory_test.set_test_fixture_result(self, test_id, fixture_id, results, target=1, timeout=timeout)

    async def get_test_fixture_result(self, test_id, timeout=None):
        '''get_test_fixture_result

        :param uint16_t test_id:  
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: fixture_id(uint16_t array), results(uint32_t array)
        '''
        return await factory_test.get_test_fixture_result(self, test_id, target=1, timeout=timeout)

    async def get_factory_mode_challenge(self, target, timeout=None):
        '''get_factory_mode_challenge

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: security_challenge(uint32_t array)
        '''
        return await factory_test.get_factory_mode_challenge(self, target, timeout=timeout)

    async def enter_factory_mode(self, security_response, target, timeout=None):
        '''enter_factory_mode

        :param uint32_t security_response:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await factory_test.enter_factory_mode(self, security_response, target, timeout=timeout)

    async def exit_factory_mode(self, target, timeout=None):
        '''exit_factory_mode

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await factory_test.exit_factory_mode(self, target, timeout=timeout)

    async def get_chassis_id(self, target, timeout=None):
        '''get_chassis_id

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: identifier(uint16_t array)
        '''
        return await factory_test.get_chassis_id(self, target, timeout=timeout)

    async def enable_extended_life_test(self, is_enabled, timeout=None):
        '''enable_extended_life_test

        :param bool is_enabled:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await factory_test.enable_extended_life_test(self, is_enabled, target=1, timeout=timeout)

    async def get_factory_mode_status(self, target, timeout=None):
        '''get_factory_mode_status

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: factory_status(bool array)
        '''
        return await factory_test.get_factory_mode_status(self, target, timeout=timeout)
