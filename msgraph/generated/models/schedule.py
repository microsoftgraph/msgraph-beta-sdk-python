from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, offer_shift_request, open_shift, open_shift_change_request, operation_status, scheduling_group, shift, swap_shifts_change_request, time_card, time_clock_settings, time_off, time_off_reason, time_off_request

from . import entity

@dataclass
class Schedule(entity.Entity):
    # Indicates whether the schedule is enabled for the team. Required.
    enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offerShiftRequests property
    offer_shift_requests: Optional[List[offer_shift_request.OfferShiftRequest]] = None
    # Indicates whether offer shift requests are enabled for the schedule.
    offer_shift_requests_enabled: Optional[bool] = None
    # The open shift requests in the schedule.
    open_shift_change_requests: Optional[List[open_shift_change_request.OpenShiftChangeRequest]] = None
    # The set of open shifts in a scheduling group in the schedule.
    open_shifts: Optional[List[open_shift.OpenShift]] = None
    # Indicates whether open shifts are enabled for the schedule.
    open_shifts_enabled: Optional[bool] = None
    # The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
    provision_status: Optional[operation_status.OperationStatus] = None
    # Additional information about why schedule provisioning failed.
    provision_status_code: Optional[str] = None
    # The logical grouping of users in the schedule (usually by role).
    scheduling_groups: Optional[List[scheduling_group.SchedulingGroup]] = None
    # The shifts in the schedule.
    shifts: Optional[List[shift.Shift]] = None
    # The swap requests for shifts in the schedule.
    swap_shifts_change_requests: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]] = None
    # Indicates whether swap shifts requests are enabled for the schedule.
    swap_shifts_requests_enabled: Optional[bool] = None
    # The timeCards property
    time_cards: Optional[List[time_card.TimeCard]] = None
    # Indicates whether time clock is enabled for the schedule.
    time_clock_enabled: Optional[bool] = None
    # The timeClockSettings property
    time_clock_settings: Optional[time_clock_settings.TimeClockSettings] = None
    # The set of reasons for a time off in the schedule.
    time_off_reasons: Optional[List[time_off_reason.TimeOffReason]] = None
    # The time off requests in the schedule.
    time_off_requests: Optional[List[time_off_request.TimeOffRequest]] = None
    # Indicates whether time off requests are enabled for the schedule.
    time_off_requests_enabled: Optional[bool] = None
    # Indicates the time zone of the schedule team using tz database format. Required.
    time_zone: Optional[str] = None
    # The instances of times off in the schedule.
    times_off: Optional[List[time_off.TimeOff]] = None
    # The workforceIntegrationIds property
    workforce_integration_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Schedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Schedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Schedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, offer_shift_request, open_shift, open_shift_change_request, operation_status, scheduling_group, shift, swap_shifts_change_request, time_card, time_clock_settings, time_off, time_off_reason, time_off_request

        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "offerShiftRequests": lambda n : setattr(self, 'offer_shift_requests', n.get_collection_of_object_values(offer_shift_request.OfferShiftRequest)),
            "offerShiftRequestsEnabled": lambda n : setattr(self, 'offer_shift_requests_enabled', n.get_bool_value()),
            "openShifts": lambda n : setattr(self, 'open_shifts', n.get_collection_of_object_values(open_shift.OpenShift)),
            "openShiftsEnabled": lambda n : setattr(self, 'open_shifts_enabled', n.get_bool_value()),
            "openShiftChangeRequests": lambda n : setattr(self, 'open_shift_change_requests', n.get_collection_of_object_values(open_shift_change_request.OpenShiftChangeRequest)),
            "provisionStatus": lambda n : setattr(self, 'provision_status', n.get_enum_value(operation_status.OperationStatus)),
            "provisionStatusCode": lambda n : setattr(self, 'provision_status_code', n.get_str_value()),
            "schedulingGroups": lambda n : setattr(self, 'scheduling_groups', n.get_collection_of_object_values(scheduling_group.SchedulingGroup)),
            "shifts": lambda n : setattr(self, 'shifts', n.get_collection_of_object_values(shift.Shift)),
            "swapShiftsChangeRequests": lambda n : setattr(self, 'swap_shifts_change_requests', n.get_collection_of_object_values(swap_shifts_change_request.SwapShiftsChangeRequest)),
            "swapShiftsRequestsEnabled": lambda n : setattr(self, 'swap_shifts_requests_enabled', n.get_bool_value()),
            "timesOff": lambda n : setattr(self, 'times_off', n.get_collection_of_object_values(time_off.TimeOff)),
            "timeCards": lambda n : setattr(self, 'time_cards', n.get_collection_of_object_values(time_card.TimeCard)),
            "timeClockEnabled": lambda n : setattr(self, 'time_clock_enabled', n.get_bool_value()),
            "timeClockSettings": lambda n : setattr(self, 'time_clock_settings', n.get_object_value(time_clock_settings.TimeClockSettings)),
            "timeOffReasons": lambda n : setattr(self, 'time_off_reasons', n.get_collection_of_object_values(time_off_reason.TimeOffReason)),
            "timeOffRequests": lambda n : setattr(self, 'time_off_requests', n.get_collection_of_object_values(time_off_request.TimeOffRequest)),
            "timeOffRequestsEnabled": lambda n : setattr(self, 'time_off_requests_enabled', n.get_bool_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "workforceIntegrationIds": lambda n : setattr(self, 'workforce_integration_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_object_values("offerShiftRequests", self.offer_shift_requests)
        writer.write_bool_value("offerShiftRequestsEnabled", self.offer_shift_requests_enabled)
        writer.write_collection_of_object_values("openShifts", self.open_shifts)
        writer.write_bool_value("openShiftsEnabled", self.open_shifts_enabled)
        writer.write_collection_of_object_values("openShiftChangeRequests", self.open_shift_change_requests)
        writer.write_collection_of_object_values("schedulingGroups", self.scheduling_groups)
        writer.write_collection_of_object_values("shifts", self.shifts)
        writer.write_collection_of_object_values("swapShiftsChangeRequests", self.swap_shifts_change_requests)
        writer.write_bool_value("swapShiftsRequestsEnabled", self.swap_shifts_requests_enabled)
        writer.write_collection_of_object_values("timesOff", self.times_off)
        writer.write_collection_of_object_values("timeCards", self.time_cards)
        writer.write_bool_value("timeClockEnabled", self.time_clock_enabled)
        writer.write_object_value("timeClockSettings", self.time_clock_settings)
        writer.write_collection_of_object_values("timeOffReasons", self.time_off_reasons)
        writer.write_collection_of_object_values("timeOffRequests", self.time_off_requests)
        writer.write_bool_value("timeOffRequestsEnabled", self.time_off_requests_enabled)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_collection_of_primitive_values("workforceIntegrationIds", self.workforce_integration_ids)
    

