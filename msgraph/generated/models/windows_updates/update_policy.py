from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_change, compliance_change_rule, deployment_audience, deployment_settings
    from .. import entity

from .. import entity

@dataclass
class UpdatePolicy(entity.Entity):
    # Specifies the audience to target.
    audience: Optional[deployment_audience.DeploymentAudience] = None
    # Rules for governing the automatic creation of compliance changes.
    compliance_change_rules: Optional[List[compliance_change_rule.ComplianceChangeRule]] = None
    # Compliance changes like content approvals which result in the automatic creation of deployments using the audience and deploymentSettings of the policy.
    compliance_changes: Optional[List[compliance_change.ComplianceChange]] = None
    # The date and time when the update policy was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # Settings for governing how to deploy content.
    deployment_settings: Optional[deployment_settings.DeploymentSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdatePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_change, compliance_change_rule, deployment_audience, deployment_settings
        from .. import entity

        from . import compliance_change, compliance_change_rule, deployment_audience, deployment_settings
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(deployment_audience.DeploymentAudience)),
            "complianceChangeRules": lambda n : setattr(self, 'compliance_change_rules', n.get_collection_of_object_values(compliance_change_rule.ComplianceChangeRule)),
            "complianceChanges": lambda n : setattr(self, 'compliance_changes', n.get_collection_of_object_values(compliance_change.ComplianceChange)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(deployment_settings.DeploymentSettings)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("audience", self.audience)
        writer.write_collection_of_object_values("complianceChangeRules", self.compliance_change_rules)
        writer.write_collection_of_object_values("complianceChanges", self.compliance_changes)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
    

