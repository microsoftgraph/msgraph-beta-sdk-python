from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account_target_content, email_identity, entity, payload, payload_delivery_platform, simulation_attack_technique, simulation_attack_type, simulation_report, simulation_status

from . import entity

class Simulation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new simulation and sets the default values.
        """
        super().__init__()
        # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        self._attack_technique: Optional[simulation_attack_technique.SimulationAttackTechnique] = None
        # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        self._attack_type: Optional[simulation_attack_type.SimulationAttackType] = None
        # Unique identifier for the attack simulation automation.
        self._automation_id: Optional[str] = None
        # Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        self._completion_date_time: Optional[datetime] = None
        # Identity of the user who created the attack simulation and training campaign.
        self._created_by: Optional[email_identity.EmailIdentity] = None
        # Date and time of creation of the attack simulation and training campaign.
        self._created_date_time: Optional[datetime] = None
        # Description of the attack simulation and training campaign.
        self._description: Optional[str] = None
        # Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        self._display_name: Optional[str] = None
        # Simulation duration in days.
        self._duration_in_days: Optional[int] = None
        # Users excluded from the simulation.
        self._excluded_account_target: Optional[account_target_content.AccountTargetContent] = None
        # Users targeted in the simulation.
        self._included_account_target: Optional[account_target_content.AccountTargetContent] = None
        # Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        self._is_automated: Optional[bool] = None
        # Identity of the user who most recently modified the attack simulation and training campaign.
        self._last_modified_by: Optional[email_identity.EmailIdentity] = None
        # Date and time of the most recent modification of the attack simulation and training campaign.
        self._last_modified_date_time: Optional[datetime] = None
        # Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        self._launch_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The payload associated with a simulation during its creation.
        self._payload: Optional[payload.Payload] = None
        # Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        self._payload_delivery_platform: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None
        # Report of the attack simulation and training campaign.
        self._report: Optional[simulation_report.SimulationReport] = None
        # Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        self._status: Optional[simulation_status.SimulationStatus] = None
    
    @property
    def attack_technique(self,) -> Optional[simulation_attack_technique.SimulationAttackTechnique]:
        """
        Gets the attackTechnique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Returns: Optional[simulation_attack_technique.SimulationAttackTechnique]
        """
        return self._attack_technique
    
    @attack_technique.setter
    def attack_technique(self,value: Optional[simulation_attack_technique.SimulationAttackTechnique] = None) -> None:
        """
        Sets the attackTechnique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Args:
            value: Value to set for the attack_technique property.
        """
        self._attack_technique = value
    
    @property
    def attack_type(self,) -> Optional[simulation_attack_type.SimulationAttackType]:
        """
        Gets the attackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Returns: Optional[simulation_attack_type.SimulationAttackType]
        """
        return self._attack_type
    
    @attack_type.setter
    def attack_type(self,value: Optional[simulation_attack_type.SimulationAttackType] = None) -> None:
        """
        Sets the attackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Args:
            value: Value to set for the attack_type property.
        """
        self._attack_type = value
    
    @property
    def automation_id(self,) -> Optional[str]:
        """
        Gets the automationId property value. Unique identifier for the attack simulation automation.
        Returns: Optional[str]
        """
        return self._automation_id
    
    @automation_id.setter
    def automation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the automationId property value. Unique identifier for the attack simulation automation.
        Args:
            value: Value to set for the automation_id property.
        """
        self._automation_id = value
    
    @property
    def completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the completionDateTime property value. Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[datetime]
        """
        return self._completion_date_time
    
    @completion_date_time.setter
    def completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completionDateTime property value. Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the completion_date_time property.
        """
        self._completion_date_time = value
    
    @property
    def created_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the createdBy property value. Identity of the user who created the attack simulation and training campaign.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the attack simulation and training campaign.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of creation of the attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of creation of the attack simulation and training campaign.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Simulation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Simulation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Simulation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the attack simulation and training campaign.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the attack simulation and training campaign.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. Simulation duration in days.
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. Simulation duration in days.
        Args:
            value: Value to set for the duration_in_days property.
        """
        self._duration_in_days = value
    
    @property
    def excluded_account_target(self,) -> Optional[account_target_content.AccountTargetContent]:
        """
        Gets the excludedAccountTarget property value. Users excluded from the simulation.
        Returns: Optional[account_target_content.AccountTargetContent]
        """
        return self._excluded_account_target
    
    @excluded_account_target.setter
    def excluded_account_target(self,value: Optional[account_target_content.AccountTargetContent] = None) -> None:
        """
        Sets the excludedAccountTarget property value. Users excluded from the simulation.
        Args:
            value: Value to set for the excluded_account_target property.
        """
        self._excluded_account_target = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account_target_content, email_identity, entity, payload, payload_delivery_platform, simulation_attack_technique, simulation_attack_type, simulation_report, simulation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "attackTechnique": lambda n : setattr(self, 'attack_technique', n.get_enum_value(simulation_attack_technique.SimulationAttackTechnique)),
            "attackType": lambda n : setattr(self, 'attack_type', n.get_enum_value(simulation_attack_type.SimulationAttackType)),
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "excludedAccountTarget": lambda n : setattr(self, 'excluded_account_target', n.get_object_value(account_target_content.AccountTargetContent)),
            "includedAccountTarget": lambda n : setattr(self, 'included_account_target', n.get_object_value(account_target_content.AccountTargetContent)),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "launchDateTime": lambda n : setattr(self, 'launch_date_time', n.get_datetime_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_object_value(payload.Payload)),
            "payloadDeliveryPlatform": lambda n : setattr(self, 'payload_delivery_platform', n.get_enum_value(payload_delivery_platform.PayloadDeliveryPlatform)),
            "report": lambda n : setattr(self, 'report', n.get_object_value(simulation_report.SimulationReport)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_status.SimulationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def included_account_target(self,) -> Optional[account_target_content.AccountTargetContent]:
        """
        Gets the includedAccountTarget property value. Users targeted in the simulation.
        Returns: Optional[account_target_content.AccountTargetContent]
        """
        return self._included_account_target
    
    @included_account_target.setter
    def included_account_target(self,value: Optional[account_target_content.AccountTargetContent] = None) -> None:
        """
        Sets the includedAccountTarget property value. Users targeted in the simulation.
        Args:
            value: Value to set for the included_account_target property.
        """
        self._included_account_target = value
    
    @property
    def is_automated(self,) -> Optional[bool]:
        """
        Gets the isAutomated property value. Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        Returns: Optional[bool]
        """
        return self._is_automated
    
    @is_automated.setter
    def is_automated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomated property value. Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        Args:
            value: Value to set for the is_automated property.
        """
        self._is_automated = value
    
    @property
    def last_modified_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time of the most recent modification of the attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time of the most recent modification of the attack simulation and training campaign.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def launch_date_time(self,) -> Optional[datetime]:
        """
        Gets the launchDateTime property value. Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[datetime]
        """
        return self._launch_date_time
    
    @launch_date_time.setter
    def launch_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the launchDateTime property value. Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the launch_date_time property.
        """
        self._launch_date_time = value
    
    @property
    def payload(self,) -> Optional[payload.Payload]:
        """
        Gets the payload property value. The payload associated with a simulation during its creation.
        Returns: Optional[payload.Payload]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[payload.Payload] = None) -> None:
        """
        Sets the payload property value. The payload associated with a simulation during its creation.
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def payload_delivery_platform(self,) -> Optional[payload_delivery_platform.PayloadDeliveryPlatform]:
        """
        Gets the payloadDeliveryPlatform property value. Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Returns: Optional[payload_delivery_platform.PayloadDeliveryPlatform]
        """
        return self._payload_delivery_platform
    
    @payload_delivery_platform.setter
    def payload_delivery_platform(self,value: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None) -> None:
        """
        Sets the payloadDeliveryPlatform property value. Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Args:
            value: Value to set for the payload_delivery_platform property.
        """
        self._payload_delivery_platform = value
    
    @property
    def report(self,) -> Optional[simulation_report.SimulationReport]:
        """
        Gets the report property value. Report of the attack simulation and training campaign.
        Returns: Optional[simulation_report.SimulationReport]
        """
        return self._report
    
    @report.setter
    def report(self,value: Optional[simulation_report.SimulationReport] = None) -> None:
        """
        Sets the report property value. Report of the attack simulation and training campaign.
        Args:
            value: Value to set for the report property.
        """
        self._report = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("attackTechnique", self.attack_technique)
        writer.write_enum_value("attackType", self.attack_type)
        writer.write_str_value("automationId", self.automation_id)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_object_value("excludedAccountTarget", self.excluded_account_target)
        writer.write_object_value("includedAccountTarget", self.included_account_target)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("launchDateTime", self.launch_date_time)
        writer.write_object_value("payload", self.payload)
        writer.write_enum_value("payloadDeliveryPlatform", self.payload_delivery_platform)
        writer.write_object_value("report", self.report)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[simulation_status.SimulationStatus]:
        """
        Gets the status property value. Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        Returns: Optional[simulation_status.SimulationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_status.SimulationStatus] = None) -> None:
        """
        Sets the status property value. Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

