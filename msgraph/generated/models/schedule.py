from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, offer_shift_request, open_shift, open_shift_change_request, operation_status, scheduling_group, shift, swap_shifts_change_request, time_card, time_clock_settings, time_off, time_off_reason, time_off_request

from . import entity

class Schedule(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new schedule and sets the default values.
        """
        super().__init__()
        # Indicates whether the schedule is enabled for the team. Required.
        self._enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The offerShiftRequests property
        self._offer_shift_requests: Optional[List[offer_shift_request.OfferShiftRequest]] = None
        # Indicates whether offer shift requests are enabled for the schedule.
        self._offer_shift_requests_enabled: Optional[bool] = None
        # The openShiftChangeRequests property
        self._open_shift_change_requests: Optional[List[open_shift_change_request.OpenShiftChangeRequest]] = None
        # The openShifts property
        self._open_shifts: Optional[List[open_shift.OpenShift]] = None
        # Indicates whether open shifts are enabled for the schedule.
        self._open_shifts_enabled: Optional[bool] = None
        # The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        self._provision_status: Optional[operation_status.OperationStatus] = None
        # Additional information about why schedule provisioning failed.
        self._provision_status_code: Optional[str] = None
        # The logical grouping of users in the schedule (usually by role).
        self._scheduling_groups: Optional[List[scheduling_group.SchedulingGroup]] = None
        # The shifts in the schedule.
        self._shifts: Optional[List[shift.Shift]] = None
        # The swapShiftsChangeRequests property
        self._swap_shifts_change_requests: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]] = None
        # Indicates whether swap shifts requests are enabled for the schedule.
        self._swap_shifts_requests_enabled: Optional[bool] = None
        # The timeCards property
        self._time_cards: Optional[List[time_card.TimeCard]] = None
        # Indicates whether time clock is enabled for the schedule.
        self._time_clock_enabled: Optional[bool] = None
        # The timeClockSettings property
        self._time_clock_settings: Optional[time_clock_settings.TimeClockSettings] = None
        # The set of reasons for a time off in the schedule.
        self._time_off_reasons: Optional[List[time_off_reason.TimeOffReason]] = None
        # The timeOffRequests property
        self._time_off_requests: Optional[List[time_off_request.TimeOffRequest]] = None
        # Indicates whether time off requests are enabled for the schedule.
        self._time_off_requests_enabled: Optional[bool] = None
        # Indicates the time zone of the schedule team using tz database format. Required.
        self._time_zone: Optional[str] = None
        # The instances of times off in the schedule.
        self._times_off: Optional[List[time_off.TimeOff]] = None
        # The workforceIntegrationIds property
        self._workforce_integration_ids: Optional[List[str]] = None
    
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
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Indicates whether the schedule is enabled for the team. Required.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Indicates whether the schedule is enabled for the team. Required.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
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
    
    @property
    def offer_shift_requests(self,) -> Optional[List[offer_shift_request.OfferShiftRequest]]:
        """
        Gets the offerShiftRequests property value. The offerShiftRequests property
        Returns: Optional[List[offer_shift_request.OfferShiftRequest]]
        """
        return self._offer_shift_requests
    
    @offer_shift_requests.setter
    def offer_shift_requests(self,value: Optional[List[offer_shift_request.OfferShiftRequest]] = None) -> None:
        """
        Sets the offerShiftRequests property value. The offerShiftRequests property
        Args:
            value: Value to set for the offer_shift_requests property.
        """
        self._offer_shift_requests = value
    
    @property
    def offer_shift_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the offerShiftRequestsEnabled property value. Indicates whether offer shift requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._offer_shift_requests_enabled
    
    @offer_shift_requests_enabled.setter
    def offer_shift_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the offerShiftRequestsEnabled property value. Indicates whether offer shift requests are enabled for the schedule.
        Args:
            value: Value to set for the offer_shift_requests_enabled property.
        """
        self._offer_shift_requests_enabled = value
    
    @property
    def open_shift_change_requests(self,) -> Optional[List[open_shift_change_request.OpenShiftChangeRequest]]:
        """
        Gets the openShiftChangeRequests property value. The openShiftChangeRequests property
        Returns: Optional[List[open_shift_change_request.OpenShiftChangeRequest]]
        """
        return self._open_shift_change_requests
    
    @open_shift_change_requests.setter
    def open_shift_change_requests(self,value: Optional[List[open_shift_change_request.OpenShiftChangeRequest]] = None) -> None:
        """
        Sets the openShiftChangeRequests property value. The openShiftChangeRequests property
        Args:
            value: Value to set for the open_shift_change_requests property.
        """
        self._open_shift_change_requests = value
    
    @property
    def open_shifts(self,) -> Optional[List[open_shift.OpenShift]]:
        """
        Gets the openShifts property value. The openShifts property
        Returns: Optional[List[open_shift.OpenShift]]
        """
        return self._open_shifts
    
    @open_shifts.setter
    def open_shifts(self,value: Optional[List[open_shift.OpenShift]] = None) -> None:
        """
        Sets the openShifts property value. The openShifts property
        Args:
            value: Value to set for the open_shifts property.
        """
        self._open_shifts = value
    
    @property
    def open_shifts_enabled(self,) -> Optional[bool]:
        """
        Gets the openShiftsEnabled property value. Indicates whether open shifts are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._open_shifts_enabled
    
    @open_shifts_enabled.setter
    def open_shifts_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the openShiftsEnabled property value. Indicates whether open shifts are enabled for the schedule.
        Args:
            value: Value to set for the open_shifts_enabled property.
        """
        self._open_shifts_enabled = value
    
    @property
    def provision_status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the provisionStatus property value. The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._provision_status
    
    @provision_status.setter
    def provision_status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the provisionStatus property value. The status of the schedule provisioning. The possible values are notStarted, running, completed, failed.
        Args:
            value: Value to set for the provision_status property.
        """
        self._provision_status = value
    
    @property
    def provision_status_code(self,) -> Optional[str]:
        """
        Gets the provisionStatusCode property value. Additional information about why schedule provisioning failed.
        Returns: Optional[str]
        """
        return self._provision_status_code
    
    @provision_status_code.setter
    def provision_status_code(self,value: Optional[str] = None) -> None:
        """
        Sets the provisionStatusCode property value. Additional information about why schedule provisioning failed.
        Args:
            value: Value to set for the provision_status_code property.
        """
        self._provision_status_code = value
    
    @property
    def scheduling_groups(self,) -> Optional[List[scheduling_group.SchedulingGroup]]:
        """
        Gets the schedulingGroups property value. The logical grouping of users in the schedule (usually by role).
        Returns: Optional[List[scheduling_group.SchedulingGroup]]
        """
        return self._scheduling_groups
    
    @scheduling_groups.setter
    def scheduling_groups(self,value: Optional[List[scheduling_group.SchedulingGroup]] = None) -> None:
        """
        Sets the schedulingGroups property value. The logical grouping of users in the schedule (usually by role).
        Args:
            value: Value to set for the scheduling_groups property.
        """
        self._scheduling_groups = value
    
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
    
    @property
    def shifts(self,) -> Optional[List[shift.Shift]]:
        """
        Gets the shifts property value. The shifts in the schedule.
        Returns: Optional[List[shift.Shift]]
        """
        return self._shifts
    
    @shifts.setter
    def shifts(self,value: Optional[List[shift.Shift]] = None) -> None:
        """
        Sets the shifts property value. The shifts in the schedule.
        Args:
            value: Value to set for the shifts property.
        """
        self._shifts = value
    
    @property
    def swap_shifts_change_requests(self,) -> Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]]:
        """
        Gets the swapShiftsChangeRequests property value. The swapShiftsChangeRequests property
        Returns: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]]
        """
        return self._swap_shifts_change_requests
    
    @swap_shifts_change_requests.setter
    def swap_shifts_change_requests(self,value: Optional[List[swap_shifts_change_request.SwapShiftsChangeRequest]] = None) -> None:
        """
        Sets the swapShiftsChangeRequests property value. The swapShiftsChangeRequests property
        Args:
            value: Value to set for the swap_shifts_change_requests property.
        """
        self._swap_shifts_change_requests = value
    
    @property
    def swap_shifts_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the swapShiftsRequestsEnabled property value. Indicates whether swap shifts requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._swap_shifts_requests_enabled
    
    @swap_shifts_requests_enabled.setter
    def swap_shifts_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the swapShiftsRequestsEnabled property value. Indicates whether swap shifts requests are enabled for the schedule.
        Args:
            value: Value to set for the swap_shifts_requests_enabled property.
        """
        self._swap_shifts_requests_enabled = value
    
    @property
    def time_cards(self,) -> Optional[List[time_card.TimeCard]]:
        """
        Gets the timeCards property value. The timeCards property
        Returns: Optional[List[time_card.TimeCard]]
        """
        return self._time_cards
    
    @time_cards.setter
    def time_cards(self,value: Optional[List[time_card.TimeCard]] = None) -> None:
        """
        Sets the timeCards property value. The timeCards property
        Args:
            value: Value to set for the time_cards property.
        """
        self._time_cards = value
    
    @property
    def time_clock_enabled(self,) -> Optional[bool]:
        """
        Gets the timeClockEnabled property value. Indicates whether time clock is enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._time_clock_enabled
    
    @time_clock_enabled.setter
    def time_clock_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the timeClockEnabled property value. Indicates whether time clock is enabled for the schedule.
        Args:
            value: Value to set for the time_clock_enabled property.
        """
        self._time_clock_enabled = value
    
    @property
    def time_clock_settings(self,) -> Optional[time_clock_settings.TimeClockSettings]:
        """
        Gets the timeClockSettings property value. The timeClockSettings property
        Returns: Optional[time_clock_settings.TimeClockSettings]
        """
        return self._time_clock_settings
    
    @time_clock_settings.setter
    def time_clock_settings(self,value: Optional[time_clock_settings.TimeClockSettings] = None) -> None:
        """
        Sets the timeClockSettings property value. The timeClockSettings property
        Args:
            value: Value to set for the time_clock_settings property.
        """
        self._time_clock_settings = value
    
    @property
    def time_off_reasons(self,) -> Optional[List[time_off_reason.TimeOffReason]]:
        """
        Gets the timeOffReasons property value. The set of reasons for a time off in the schedule.
        Returns: Optional[List[time_off_reason.TimeOffReason]]
        """
        return self._time_off_reasons
    
    @time_off_reasons.setter
    def time_off_reasons(self,value: Optional[List[time_off_reason.TimeOffReason]] = None) -> None:
        """
        Sets the timeOffReasons property value. The set of reasons for a time off in the schedule.
        Args:
            value: Value to set for the time_off_reasons property.
        """
        self._time_off_reasons = value
    
    @property
    def time_off_requests(self,) -> Optional[List[time_off_request.TimeOffRequest]]:
        """
        Gets the timeOffRequests property value. The timeOffRequests property
        Returns: Optional[List[time_off_request.TimeOffRequest]]
        """
        return self._time_off_requests
    
    @time_off_requests.setter
    def time_off_requests(self,value: Optional[List[time_off_request.TimeOffRequest]] = None) -> None:
        """
        Sets the timeOffRequests property value. The timeOffRequests property
        Args:
            value: Value to set for the time_off_requests property.
        """
        self._time_off_requests = value
    
    @property
    def time_off_requests_enabled(self,) -> Optional[bool]:
        """
        Gets the timeOffRequestsEnabled property value. Indicates whether time off requests are enabled for the schedule.
        Returns: Optional[bool]
        """
        return self._time_off_requests_enabled
    
    @time_off_requests_enabled.setter
    def time_off_requests_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the timeOffRequestsEnabled property value. Indicates whether time off requests are enabled for the schedule.
        Args:
            value: Value to set for the time_off_requests_enabled property.
        """
        self._time_off_requests_enabled = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. Indicates the time zone of the schedule team using tz database format. Required.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. Indicates the time zone of the schedule team using tz database format. Required.
        Args:
            value: Value to set for the time_zone property.
        """
        self._time_zone = value
    
    @property
    def times_off(self,) -> Optional[List[time_off.TimeOff]]:
        """
        Gets the timesOff property value. The instances of times off in the schedule.
        Returns: Optional[List[time_off.TimeOff]]
        """
        return self._times_off
    
    @times_off.setter
    def times_off(self,value: Optional[List[time_off.TimeOff]] = None) -> None:
        """
        Sets the timesOff property value. The instances of times off in the schedule.
        Args:
            value: Value to set for the times_off property.
        """
        self._times_off = value
    
    @property
    def workforce_integration_ids(self,) -> Optional[List[str]]:
        """
        Gets the workforceIntegrationIds property value. The workforceIntegrationIds property
        Returns: Optional[List[str]]
        """
        return self._workforce_integration_ids
    
    @workforce_integration_ids.setter
    def workforce_integration_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the workforceIntegrationIds property value. The workforceIntegrationIds property
        Args:
            value: Value to set for the workforce_integration_ids property.
        """
        self._workforce_integration_ids = value
    

